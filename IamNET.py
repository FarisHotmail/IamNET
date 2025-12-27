import sys
import os
import platform
import subprocess
import time

# --- ADIM 1: KRİTİK KÜTÜPHANE KONTROLÜ (GUI Öncesi) ---
def check_tkinter():
    try:
        import tkinter
        return True
    except ImportError:
        system_os = platform.system()
        print("\n!!! KRİTİK EKSİK: 'tkinter' kütüphanesi bulunamadı. !!!")
        print("Arayüzün çalışması için bu kütüphane şarttır.\n")
        
        if system_os == "Linux":
            print("Linux tespit edildi.")
            try:
                # Kullanıcıdan onay iste
                choice = input("Gerekli paketleri (python3-tk) otomatik yüklemeyi deneyeyim mi? (E/H): ").strip().lower()
                if choice == 'e':
                    print("Yükleme başlıyor (Sudo şifresi gerekebilir)...")
                    subprocess.check_call(['sudo', 'apt-get', 'update'])
                    subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'python3-tk'])
                    print("\nYükleme tamamlandı! Lütfen uygulamayı TEKRAR çalıştırın.")
                    sys.exit()
                else:
                    print("\nManuel Yükleme İçin Terminale Şu Komutu Yazın:")
                    print("sudo apt-get install python3-tk")
            except Exception as e:
                print(f"\nOtomatik yükleme başarısız oldu: {e}")
                print("Lütfen manuel yükleyin: sudo apt-get install python3-tk")
        else:
            # Windows/MacOS
            print("Windows/Mac üzerinde Python kurulumunuzda 'tcl/tk' seçeneği eksik veya bozuk.")
            print("Lütfen Python'u 'Modify' seçeneği ile onarın veya yeniden kurun.")
        
        input("\nÇıkmak için Enter'a basın...")
        sys.exit()

# Kontrolü çalıştır
check_tkinter()

# --- ADIM 2: DİĞER KÜTÜPHANELER ---
try:
    import customtkinter as ctk
    import speedtest
    import requests
    import psutil
except ImportError as e:
    print(f"\nEksik Kütüphane Tespit Edildi: {e.name}")
    print("Lütfen şu komutu çalıştırın: pip install customtkinter speedtest-cli requests psutil")
    input("Çıkmak için Enter'a basın...")
    sys.exit()

import csv
import threading
import json
import socket
from datetime import datetime
from tkinter import filedialog

# --- SABİTLER VE AYARLAR ---
CONFIG_FILE = "config.json"
SERVER_LIST_FILE = "server_list.csv"

# Akıllı Dizin Bulucu
def get_smart_directory():
    """Kullanıcının Masaüstünü veya güvenli bir yazılabilir alanı bulur."""
    home = os.path.expanduser("~")
    
    # 1. Standart Desktop
    desktop = os.path.join(home, "Desktop")
    if os.path.exists(desktop): return desktop
    
    # 2. Yerelleştirilmiş (Örn: Türkçe Linux)
    tr_desktop = os.path.join(home, "Masaüstü")
    if os.path.exists(tr_desktop): return tr_desktop
    
    # 3. OneDrive Desktop (Windows Yaygın Sorunu)
    onedrive_desk = os.path.join(home, "OneDrive", "Desktop")
    if os.path.exists(onedrive_desk): return onedrive_desk
    
    # 4. Fallback: Belgelerim
    documents = os.path.join(home, "Documents")
    if os.path.exists(documents): return documents
    
    # 5. Hiçbiri yoksa Home
    return home

# Dil Veritabanı
LANGUAGES = {
    "TR": "Türkçe", "EN": "English", "DE": "Deutsch",
    "FR": "Français", "ES": "Español", "RU": "Русский"
}

TRANSLATIONS = {
    "TR": {
        "app_title": "IamNET - Ağ Analiz",
        "menu_dash": "Kontrol Paneli",
        "menu_settings": "Ayarlar",
        "status_ready": "Hazır",
        "status_running": "Test Çalışıyor...",
        "status_done": "Tamamlandı",
        "btn_start": "TESTİ BAŞLAT",
        "btn_stop": "DURDUR",
        "log_stop_req": "Durdurma isteği alındı...",
        "settings_title": "Uygulama Ayarları",
        "lang_sel": "Dil Seçimi / Language",
        "lang_desc": "Arayüz dilini değiştirir.",
        "dir_lbl": "Kayıt Dizini",
        "dir_desc": "Sonuçların kaydedileceği klasör.",
        "fname_dom_lbl": "Yurtiçi Dosya Adı",
        "fname_dom_desc": "Yerel test dosyası.",
        "fname_for_lbl": "Yurtdışı Dosya Adı",
        "fname_for_desc": "Yurtdışı test dosyası.",
        "srv_count_lbl": "Sunucu Sayısı",
        "srv_count_desc": "Toplam test edilecek sunucu.",
        "thresh_lbl": "Trafik Eşiği (Kbps)",
        "thresh_desc": "Uyarı verilecek trafik limiti.",
        "dur_lbl": "İzleme Süresi (sn)",
        "dur_desc": "Başlamadan önceki kontrol süresi.",
        "loop_lbl": "Sonsuz Döngü",
        "loop_desc": "Test bitince başa sarar.",
        "detail_lbl": "Detaylı Log",
        "detail_desc": "Sunucu detaylarını gösterir.",
        "btn_save": "Ayarları Kaydet",
        "msg_saved": "Ayarlar Kaydedildi!",
        "err_net": "İnternet Yok!"
    },
    "EN": {
        "app_title": "IamNET - Network Analysis",
        "menu_dash": "Dashboard",
        "menu_settings": "Settings",
        "status_ready": "Ready",
        "status_running": "Running...",
        "status_done": "Completed",
        "btn_start": "START TEST",
        "btn_stop": "STOP",
        "log_stop_req": "Stopping...",
        "settings_title": "Settings",
        "lang_sel": "Language",
        "lang_desc": "Interface language.",
        "dir_lbl": "Save Directory",
        "dir_desc": "Results folder.",
        "fname_dom_lbl": "Local Filename",
        "fname_dom_desc": "Local test file.",
        "fname_for_lbl": "Foreign Filename",
        "fname_for_desc": "Foreign test file.",
        "srv_count_lbl": "Server Count",
        "srv_count_desc": "Total servers.",
        "thresh_lbl": "Threshold (Kbps)",
        "thresh_desc": "Traffic limit warning.",
        "dur_lbl": "Duration (sec)",
        "dur_desc": "Monitor time.",
        "loop_lbl": "Infinite Loop",
        "loop_desc": "Restart automatically.",
        "detail_lbl": "Detailed Log",
        "detail_desc": "Show server info.",
        "btn_save": "Save Settings",
        "msg_saved": "Settings Saved!",
        "err_net": "No Internet!"
    }
}
# (Diğer diller TR/EN yedeği kullanır, kod kısalığı için eklemedim ama mantık hazır)

DEFAULT_CONFIG = {
    "language": "TR",
    "save_dir": get_smart_directory(), # AKILLI DİZİN BURADA KULLANILIYOR
    "filename_domestic": "yurtici_sonuclari.csv",
    "filename_foreign": "yurtdisi_sonuclari.csv",
    "traffic_threshold_kbps": 500,
    "traffic_duration_sec": 4,
    "server_count": 10,
    "infinite_loop": False,
    "show_server_details": True
}

class ConfigManager:
    @staticmethod
    def load():
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Eğer config dosyasındaki save_dir silinmiş bir klasörse, akıllı dizine dön
                    cfg = {**DEFAULT_CONFIG, **data}
                    if not os.path.exists(cfg["save_dir"]):
                        cfg["save_dir"] = get_smart_directory()
                    return cfg
            except: pass
        return DEFAULT_CONFIG.copy()

    @staticmethod
    def save(config):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)

class IamNetApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        
        # İnternet Kontrolü
        if not self.check_internet_startup():
            return

        self.config_data = ConfigManager.load()
        self.lang_code = self.config_data.get("language", "TR")
        self.t_dict = TRANSLATIONS.get(self.lang_code, TRANSLATIONS["TR"])
        
        self.title(self.t("app_title"))
        self.geometry("950x750")
        
        self.is_running = False
        self.stop_event = threading.Event()
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_ui()
        self.show_dashboard()

    def t(self, key):
        val = self.t_dict.get(key)
        return val if val else TRANSLATIONS["TR"].get(key, key)

    def check_internet_startup(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            import tkinter.messagebox as mbox
            root = ctk.CTk()
            root.withdraw()
            mbox.showerror("IamNET Error", self.t("err_net"))
            root.destroy()
            self.destroy()
            return False

    def setup_ui(self):
        # SOL MENÜ
        self.sidebar = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="IamNET", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.btn_dash = ctk.CTkButton(self.sidebar, text=self.t("menu_dash"), command=self.show_dashboard)
        self.btn_dash.grid(row=1, column=0, padx=20, pady=10)
        
        self.btn_settings = ctk.CTkButton(self.sidebar, text=self.t("menu_settings"), command=self.show_settings)
        self.btn_settings.grid(row=2, column=0, padx=20, pady=10)

        # DASHBOARD
        self.frame_dash = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.info_frame = ctk.CTkFrame(self.frame_dash)
        self.info_frame.pack(fill="x", pady=(0, 20))
        self.lbl_ip = ctk.CTkLabel(self.info_frame, text="IP: ...", font=("Arial", 14))
        self.lbl_ip.pack(side="left", padx=20, pady=10)
        self.lbl_status = ctk.CTkLabel(self.info_frame, text=self.t("status_ready"), text_color="#2CC985", font=("Arial", 14, "bold"))
        self.lbl_status.pack(side="right", padx=20, pady=10)

        self.speed_frame = ctk.CTkFrame(self.frame_dash, fg_color=("gray85", "gray17"))
        self.speed_frame.pack(fill="x", pady=(0, 20))
        self.lbl_val = ctk.CTkLabel(self.speed_frame, text="0.00", font=("Roboto", 64, "bold"), text_color="#3B8ED0")
        self.lbl_val.pack(pady=(20, 0))
        self.lbl_unit = ctk.CTkLabel(self.speed_frame, text="Mbps", font=("Roboto", 20))
        self.lbl_unit.pack(pady=(0, 20))

        self.log_box = ctk.CTkTextbox(self.frame_dash, height=300, font=("Consolas", 12))
        self.log_box.pack(fill="both", expand=True)
        self.log_box.configure(state="disabled")

        self.act_frame = ctk.CTkFrame(self.frame_dash, fg_color="transparent")
        self.act_frame.pack(fill="x", pady=20)
        self.btn_start = ctk.CTkButton(self.act_frame, text=self.t("btn_start"), height=40, fg_color="green", hover_color="darkgreen", command=self.start_thread)
        self.btn_start.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.btn_stop = ctk.CTkButton(self.act_frame, text=self.t("btn_stop"), height=40, fg_color="red", hover_color="darkred", state="disabled", command=self.stop_test)
        self.btn_stop.pack(side="right", fill="x", expand=True, padx=(10, 0))

        # AYARLAR (Placeholder)
        self.frame_settings = ctk.CTkScrollableFrame(self, corner_radius=0, label_text=self.t("settings_title"))

        self.get_ip()

    def get_ip(self):
        def _fetch():
            try:
                ip = requests.get("https://api.ipify.org", timeout=5).text
                self.lbl_ip.configure(text=f"IP: {ip}")
            except:
                self.lbl_ip.configure(text="IP: N/A")
        threading.Thread(target=_fetch, daemon=True).start()

    def show_dashboard(self):
        self.frame_settings.grid_forget()
        self.frame_dash.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_settings(self):
        self.frame_dash.grid_forget()
        self.build_settings_ui()
        self.frame_settings.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def create_row_frame(self):
        f = ctk.CTkFrame(self.frame_settings, fg_color="transparent")
        f.pack(fill="x", padx=10, pady=8)
        return f

    def build_settings_ui(self):
        for widget in self.frame_settings.winfo_children():
            widget.destroy()
        
        self.frame_settings.configure(label_text=self.t("settings_title"))

        # 1. DİL
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("lang_sel"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("lang_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        lang_var = ctk.StringVar(value=LANGUAGES.get(self.lang_code, "Türkçe"))
        ctk.CTkComboBox(row, values=list(LANGUAGES.values()), variable=lang_var, width=150, command=self.change_language).pack(side="right")

        # 2. DİZİN
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("dir_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("dir_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        
        f_right = ctk.CTkFrame(row, fg_color="transparent")
        f_right.pack(side="right")
        self.entry_dir = ctk.CTkEntry(f_right, width=200)
        self.entry_dir.insert(0, self.config_data["save_dir"])
        self.entry_dir.pack(side="left", padx=(0, 5))
        ctk.CTkButton(f_right, text="...", width=30, command=self.select_dir).pack(side="left")

        # 3. YURTİÇİ
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("fname_dom_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("fname_dom_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        self.ent_dom = ctk.CTkEntry(row, width=240)
        self.ent_dom.insert(0, self.config_data["filename_domestic"])
        self.ent_dom.pack(side="right")

        # 4. YURTDIŞI
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("fname_for_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("fname_for_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        self.ent_for = ctk.CTkEntry(row, width=240)
        self.ent_for.insert(0, self.config_data["filename_foreign"])
        self.ent_for.pack(side="right")

        # 5. SUNUCU SAYISI
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("srv_count_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("srv_count_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        f_r = ctk.CTkFrame(row, fg_color="transparent")
        f_r.pack(side="right")
        self.lbl_srv_val = ctk.CTkLabel(f_r, text=str(self.config_data["server_count"]), width=30)
        self.lbl_srv_val.pack(side="left", padx=5)
        self.slider_srv = ctk.CTkSlider(f_r, from_=2, to=100, number_of_steps=98, width=150)
        self.slider_srv.set(self.config_data["server_count"])
        self.slider_srv.configure(command=lambda v: self.lbl_srv_val.configure(text=str(int(v))))
        self.slider_srv.pack(side="left")

        # 6. TRAFİK EŞİĞİ
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("thresh_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("thresh_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        self.ent_thresh = ctk.CTkEntry(row, width=100)
        self.ent_thresh.insert(0, str(self.config_data["traffic_threshold_kbps"]))
        self.ent_thresh.pack(side="right")

        # 7. SÜRE
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("dur_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("dur_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        self.ent_dur = ctk.CTkEntry(row, width=100)
        self.ent_dur.insert(0, str(self.config_data["traffic_duration_sec"]))
        self.ent_dur.pack(side="right")

        # 8. SONSUZ DÖNGÜ
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("loop_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("loop_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        self.var_loop = ctk.BooleanVar(value=self.config_data["infinite_loop"])
        ctk.CTkSwitch(row, text="", variable=self.var_loop).pack(side="right")

        # 9. DETAY
        row = self.create_row_frame()
        f_text = ctk.CTkFrame(row, fg_color="transparent")
        f_text.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(f_text, text=self.t("detail_lbl"), font=("Arial", 14, "bold")).pack(anchor="w")
        ctk.CTkLabel(f_text, text=self.t("detail_desc"), text_color="gray60", font=("Arial", 11, "italic")).pack(anchor="w")
        self.var_det = ctk.BooleanVar(value=self.config_data["show_server_details"])
        ctk.CTkSwitch(row, text="", variable=self.var_det).pack(side="right")

        # KAYDET
        f_btn = ctk.CTkFrame(self.frame_settings, fg_color="transparent")
        f_btn.pack(pady=30, fill="x")
        btn_save = ctk.CTkButton(f_btn, text=self.t("btn_save"), fg_color="green", height=40, font=("Arial", 14, "bold"), command=self.save_settings)
        btn_save.pack(side="left", padx=20)
        self.lbl_save_msg = ctk.CTkLabel(f_btn, text="", text_color="#2CC985", font=("Arial", 12, "bold"))
        self.lbl_save_msg.pack(side="left", padx=10)

    def change_language(self, choice):
        code = next((k for k, v in LANGUAGES.items() if v == choice), "TR")
        self.lang_code = code
        self.config_data["language"] = code
        self.t_dict = TRANSLATIONS.get(code, TRANSLATIONS["TR"])
        
        # Arayüzü yenile
        self.title(self.t("app_title"))
        self.btn_dash.configure(text=self.t("menu_dash"))
        self.btn_settings.configure(text=self.t("menu_settings"))
        self.lbl_status.configure(text=self.t("status_ready"))
        self.btn_start.configure(text=self.t("btn_start"))
        self.btn_stop.configure(text=self.t("btn_stop"))
        
        self.build_settings_ui()

    def select_dir(self):
        d = filedialog.askdirectory()
        if d:
            self.entry_dir.delete(0, "end")
            self.entry_dir.insert(0, d)

    def save_settings(self):
        try:
            self.config_data["save_dir"] = self.entry_dir.get()
            self.config_data["filename_domestic"] = self.ent_dom.get()
            self.config_data["filename_foreign"] = self.ent_for.get()
            self.config_data["server_count"] = int(self.slider_srv.get())
            self.config_data["traffic_threshold_kbps"] = float(self.ent_thresh.get())
            self.config_data["traffic_duration_sec"] = float(self.ent_dur.get())
            self.config_data["infinite_loop"] = self.var_loop.get()
            self.config_data["show_server_details"] = self.var_det.get()
            self.config_data["language"] = self.lang_code
            
            ConfigManager.save(self.config_data)
            self.lbl_save_msg.configure(text=self.t("msg_saved"))
            self.after(3000, lambda: self.lbl_save_msg.configure(text=""))
        except Exception as e:
            self.lbl_save_msg.configure(text=f"Err: {e}", text_color="red")

    def log(self, msg):
        self.log_box.configure(state="normal")
        ts = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{ts}] {msg}\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def start_thread(self):
        kbps_limit = self.config_data["traffic_threshold_kbps"]
        dur = self.config_data["traffic_duration_sec"]
        
        self.log(f"Analiz ediliyor ({dur}s)...")
        self.btn_start.configure(state="disabled") # Çift tıklamayı önle
        
        def _check_run():
            try:
                n1 = psutil.net_io_counters()
                time.sleep(dur)
                n2 = psutil.net_io_counters()
                
                total = (n2.bytes_recv - n1.bytes_recv) + (n2.bytes_sent - n1.bytes_sent)
                curr_kbps = (total * 8) / dur / 1000
                
                if curr_kbps > kbps_limit:
                    self.log(f"UYARI: Trafik yüksek ({curr_kbps:.2f} Kbps)!")
                
                self.is_running = True
                self.stop_event.clear()
                self.btn_stop.configure(state="normal")
                self.lbl_status.configure(text=self.t("status_running"), text_color="orange")
                
                self.run_test()
                
            except Exception as e:
                self.log(f"Başlatma Hatası: {e}")
                self.btn_start.configure(state="normal")

        threading.Thread(target=_check_run, daemon=True).start()

    def stop_test(self):
        self.stop_event.set()
        self.is_running = False
        self.log(self.t("log_stop_req"))
        self.btn_stop.configure(state="disabled")

    def run_test(self):
        st = speedtest.Speedtest()
        count = self.config_data["server_count"]
        c_for = count // 2
        c_dom = count - c_for
        
        self.log("Sunucu listesi alınıyor...")
        
        # Yurtici
        dom_list = []
        try:
            raw = st.get_servers()
            for sl in raw.values():
                for s in sl:
                    if s['country'] == 'Turkey': dom_list.append(s)
            dom_list = dom_list[:c_dom]
        except: pass
        
        # Yurtdisi
        for_list = []
        backups = [
             {'country': 'Germany', 'sponsor': 'Tele2', 'host': 'speedtest.tele2.net', 'manual_url': 'http://speedtest.tele2.net/100MB.zip'},
             {'country': 'France', 'sponsor': 'OVH', 'host': 'proof.ovh.net', 'manual_url': 'http://proof.ovh.net/files/100Mb.dat'},
             {'country': 'NL', 'sponsor': 'i3D.net', 'host': 'mirror.i3d.net', 'manual_url': 'http://mirror.i3d.net/100mb.bin'}
        ]
        try:
            raw = st.get_servers([13623, 2789, 5252])
            for sl in raw.values():
                for s in sl: for_list.append(s)
        except: pass
        
        if len(for_list) < c_for:
            needed = c_for - len(for_list)
            for i in range(needed):
                for_list.append(backups[i % len(backups)])
        
        all_s = []
        for i in range(max(len(dom_list), len(for_list))):
            if i < len(dom_list): all_s.append(dom_list[i])
            if i < len(for_list): all_s.append(for_list[i])

        # Server Log
        try:
            exists = os.path.exists(SERVER_LIST_FILE)
            with open(SERVER_LIST_FILE, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if not exists: w.writerow(["Date", "Sponsor", "Country", "Host"])
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for s in all_s:
                    w.writerow([now, s['sponsor'], s['country'], s['host']])
                    if self.config_data["show_server_details"]:
                        self.log(f"List: {s['sponsor']} ({s['country']})")
        except: pass

        while self.is_running and not self.stop_event.is_set():
            if not all_s:
                self.log("Liste Boş!")
                break

            for idx, s in enumerate(all_s):
                if self.stop_event.is_set(): break
                self.lbl_unit.configure(text=f"{s['sponsor']} ({s['country']})")
                self.log(f"Test ({idx+1}/{len(all_s)}): {s['sponsor']}")
                
                url = s.get('manual_url')
                if not url: url = f"{os.path.dirname(s['url'])}/random4000x4000.jpg"
                
                res = self.do_download(url)
                if res:
                    self.save_csv(s, res)
                    self.log(f"-> {res['avg']:.2f} Mbps")
                else:
                    self.log("-> Hata")
                time.sleep(1)

            if not self.config_data["infinite_loop"]: break
            
            if not self.stop_event.is_set():
                self.log("Döngü bitti, bekleniyor...")
                for _ in range(60):
                    if self.stop_event.is_set(): break
                    time.sleep(1)

        self.is_running = False
        self.btn_start.configure(state="normal")
        self.btn_stop.configure(state="disabled")
        self.lbl_status.configure(text=self.t("status_done"), text_color="white")
        self.lbl_val.configure(text="0.00")
        self.lbl_unit.configure(text="Mbps")
        self.log("=== Bitti ===")

    def do_download(self, url):
        try:
            speeds = []
            total = 0
            start = datetime.now()
            with requests.get(url, stream=True, timeout=10) as r:
                r.raise_for_status()
                ts = time.time()
                tcs = time.time()
                for chunk in r.iter_content(1024*128):
                    if self.stop_event.is_set() or (time.time()-ts > 15): break
                    if not chunk: break
                    tce = time.time()
                    diff = tce - tcs
                    size = len(chunk)
                    total += size
                    if diff > 0:
                        mbps = (size * 8) / (diff * 1_000_000)
                        speeds.append(mbps)
                        if len(speeds) % 4 == 0: self.lbl_val.configure(text=f"{mbps:.2f}")
                    tcs = time.time()
            end = datetime.now()
            if not speeds: return None
            return {"min": min(speeds), "max": max(speeds), "avg": sum(speeds)/len(speeds), "start": start, "end": end, "bytes": total}
        except: return None

    def save_csv(self, s, res):
        is_tr = (s['country'] == 'Turkey')
        fname = self.config_data["filename_domestic"] if is_tr else self.config_data["filename_foreign"]
        path = os.path.join(self.config_data["save_dir"], fname)
        
        if not os.path.exists(self.config_data["save_dir"]):
            os.makedirs(self.config_data["save_dir"])
            
        try:
            exists = os.path.exists(path)
            with open(path, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if not exists: w.writerow(["IP", "Host", "Sponsor", "Bytes", "Start", "End", "Min", "Max", "Avg"])
                w.writerow(["Self", s['host'], s['sponsor'], res['bytes'], res['start'], res['end'], 
                            f"{res['min']:.2f}", f"{res['max']:.2f}", f"{res['avg']:.2f}"])
        except: pass

if __name__ == "__main__":
    app = IamNetApp()
    app.mainloop()