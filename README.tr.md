<p align="right">
  <a href="README.en.md">English</a> | 
  <a href="README.de.md">Deutsch</a> | 
  <a href="README.fr.md">Français</a> | 
  <a href="README.es.md">Español</a> | 
  <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14.2-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux-lightgrey">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-blueviolet">
  <img src="https://img.shields.io/badge/Privacy-No%20Telemetry-success">
  <img src="https://img.shields.io/badge/CLI-Available-success">
</p>

### Proje Notları
Bu projede kullanılan tüm kodlar Google Studio AI aracı ile yazılmıştır ve tamamen hobi amaçlıdır. Çok sık olmasa da proje gelişmeye devam edecek.

🔷 IamNET

IamNET, çoklu yerli ve yabancı sunucular üzerinden internet hızını ölçmeyi amaçlayan,
tamamen yerel çalışan ve gizlilik odaklı bir masaüstü uygulamasıdır.

🚀 Özellikler

- Çoklu sunucu hız testi
- Yurtiçi / yurtdışı sunucu ayrımı
- Grafik kullanıcı arayüzü (CustomTkinter tabanlı)
- **Komut satırı modu (GUI'den bağımsız)**
- Trafik yükü tespiti
- CSV dışa aktarma
- Çoklu dil desteği (TR / EN hazır)
- Renkli terminal çıktısı
- Ctrl+C ile güvenli durdurma
- Telemetri yok
- Veri iletimi yok

🔐 Gizlilik Politikası (Önemli)

IamNET:
Kullanıcı verisi toplamaz
Veri göndermez
Harici sistemlere raporlama yapmaz
Sunucuya özgü hiçbir kişisel veri saklamaz

Yerel olarak saklanan dosyalar:
Dosya	Açıklama
yurtici_sonuclari.csv	Yerli sunucu test sonuçları
yurtdisi_sonuclari.csv	Yabancı sunucu test sonuçları
config.json	Uygulama ayarları

Tüm dosyalar kullanıcının kendi dizininde saklanır.

🖥️ Sistem Gereksinimleri
Python 3.14.2
Windows 10 / 11
Linux: Test edilmedi ancak büyük olasılıkla çalışır
Linux için:
sudo apt install python3-tk

⚙️ Kurulum
git clone https://github.com/FarisHotmail/IamNET.git
cd IamNET
pip install -r requirements.txt
python IamNET.py

🧭 Nasıl Çalışır?

İnternet bağlantısı kontrol edilir
Trafik yoğunluğu analiz edilir
Sunucu listesi oluşturulur
Sunucular sırayla test edilir
Sonuçlar CSV dosyalarına yazılır
GUI üzerinden anlık hız görüntülenir

### Komut Satırı Test Motoru

- Grafik arayüzünden tamamen bağımsız çalışır
- Tüm ayarlar komut satırı argümanlarıyla yapılandırılabilir
- Renkli ve okunabilir terminal günlükleri
- Ctrl+C ile güvenli durdurma
- Arka planda çalıştırma ve otomasyon için uygundur

### CLI Parametreleri

| Parametre | Kısa | Açıklama |
|---------|------|-------------|
| --cli | - | CLI modunu etkinleştir |
| --count | -c | Sunucu sayısı (2–100) |
| --loop | -l | Sonsuz test döngüsü |
| --no-traffic | - | Trafik kontrolünü atla |
| --dir | -d | Özel kayıt dizini |
| --verbose | -v | Ayrıntılı sunucu çıktısı |

### Arka Plan Çalıştırma (Linux)
Arka planda çalıştır:
nohup python IamNET.py --cli --loop > test.log 2>&1 &

Planlanmış test (crontab):
# Her gece 02:00'de çalıştır
0 2 * * * /usr/bin/python3 /path/to/IamNET.py --cli -c 30

🖥️ CLI Kullanımı

Temel CLI testi:
python IamNET.py --cli

20 farklı sunucu ile test:
python IamNET.py --cli --count 20

Sonsuz döngü:
python IamNET.py --cli --loop

Trafik doğrulamayı atla:
python IamNET.py --cli --no-traffic

Ayrıntılı çıktı:
python IamNET.py --cli --verbose

Özel kayıt dizini:
python IamNET.py --cli --dir /path/to/folder

Birleşik kullanım:
python IamNET.py --cli -c 15 -l -v

📸 Ekran Görüntüleri (GUI)
## Dashboard
![Dashboard](screenshots/dashboard.png)
## Ayarlar
![Settings](screenshots/settings.png)

❓ Sık Sorulan Sorular

IamNET speedtest.net mi kullanıyor?
→ Hayır. Speedtest altyapısından sunucu bilgileri alınır ancak testler manuel indirme ile yapılır.

Sonuçlar neden farklı çıkıyor?
→ Sunucu lokasyonu, anlık trafik ve rota değişkenliği.

VPN ile çalışır mı?
→ Evet, ancak sonuçlar VPN hızını yansıtır.

🤝 Katkı

Pull Request ve Issue’lar açıktır.
Büyük değişikliklerde önce Issue açılması önerilir.

📜 Lisans

MIT License