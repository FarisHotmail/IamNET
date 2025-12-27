<p align="right">
  <a href="README.tr.md">Türkçe</a> | 
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
  <img src="https://img.shields.io/badge/CLI-Planned-orange">
</p>

🔷 IamNET

IamNET is a desktop application designed to measure internet speed using multiple domestic and international servers.  
It operates entirely locally and is focused on user privacy.

🚀 Features

- Multi-server speed testing  
- Domestic / international server separation  
- GUI (based on CustomTkinter)  
- Network traffic intensity detection  
- CSV output support  
- Multi-language infrastructure (TR / EN ready)  
- No telemetry  
- No data transmission  

🔐 Privacy Policy (Important)

IamNET:

- Does not collect user data  
- Does not transmit data  
- Does not report to external systems  
- Does not store any server-specific personal data  

Locally stored files:

| File | Description |
|-----|------------|
| `yurtici_sonuclari.csv` | Domestic server test results |
| `yurtdisi_sonuclari.csv` | International server test results |
| `config.json` | Application settings |

All files are stored in the user’s own local directory.

🖥️ System Requirements

- Python 3.14.2  
- Windows 10 / 11  
- Linux: Not tested, but very likely to work  

For Linux:

sudo apt install python3-tk

⚙️ Installation

git clone https://github.com/FarisHotmail/IamNET.git
cd IamNET
pip install -r requirements.txt
python IamNET.py


🧭 How It Works

Internet connection is checked

Network traffic intensity is analyzed

Server list is generated

Servers are tested sequentially

Results are written to CSV files

Real-time speed is displayed via the GUI

📸 Screenshots




🛠️ Planned Features

CLI (command-line) version

Windows .exe distribution

Additional language support

Graph-based speed history

❓ Frequently Asked Questions

Does IamNET use speedtest.net?
→ No. Server information is retrieved from the Speedtest infrastructure, but tests are performed via manual file downloads.

Why do results differ?
→ Differences are caused by server location, real-time traffic, and routing variability.

Does it work with VPN?
→ Yes, but results will reflect the VPN connection speed.

🤝 Contributing

Pull Requests and Issues are welcome.
For major changes, opening an Issue first is recommended.

📜 License

MIT License