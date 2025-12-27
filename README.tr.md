<p align="right">
  <a href="README.tr.md">Türkçe</a> |
  <a href="README.en.md">English</a>
  <a href="README.de.md">Deutsch</a>
  <a href="README.fr.md">Français</a>
  <a href="README.es.md">Español</a>
  <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14.2-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux-lightgrey">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-blueviolet">
  <img src="https://img.shields.io/badge/Privacy-No%20Telemetry-success">
  <img src="https://img.shields.io/badge/CLI-Planned-orange">
</p>


🔷 IamNET

IamNET, çoklu yerli ve yabancı sunucular üzerinden internet hızını ölçmeyi amaçlayan,
tamamen yerel çalışan ve gizlilik odaklı bir masaüstü uygulamasıdır.

🚀 Özellikler

Çoklu sunucu ile hız testi

Yerli / yabancı sunucu ayrımı

GUI (CustomTkinter tabanlı)

Trafik yoğunluğu algılama

CSV çıktı desteği

Çoklu dil altyapısı (TR / EN hazır)

Telemetri yok

Veri gönderimi yok

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

📸 Ekran Görüntüleri
![Dashboard](screenshots/dashboard.png)
![Settings](screenshots/settings.png)

🛠️ Planlanan Özellikler

CLI (komut satırı) sürümü

Windows .exe dağıtımı

Daha fazla dil desteği

Grafik tabanlı hız geçmişi

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