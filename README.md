<p align="right">
  <a href="README.tr.md">Türkçe</a> | 
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

# IamNET

## Project Notes
All the code in this project was created using the Google Studio AI tool. This project is designed purely as a hobby project. Development work will be done, albeit not regularly.

## Description
IamNET is a privacy-focused desktop application designed to measure internet speed using multiple domestic and international servers.  
It operates entirely locally.

## 🚀 Features
- Multi-server speed testing
- Domestic / international server separation
- GUI (CustomTkinter-based)
- CLI mode (GUI-independent)
- Traffic load detection
- CSV export
- Multi-language support (TR / EN ready)
- Colored terminal output
- Ctrl+C safe stop
- No telemetry
- No data transmission

## 🔐 Privacy Policy
IamNET:
- Does not collect user data
- Does not transmit data
- Does not store any server-specific personal data

**Locally stored files:**

| File | Description |
|------|-------------|
| `yurtici_sonuclari.csv` | Domestic server test results |
| `yurtdisi_sonuclari.csv` | International server test results |
| `config.json` | Application settings |

## 🖥️ System Requirements
- Python 3.14.2
- Windows 10 / 11
- Linux (not officially tested)

For Linux:
```bash
sudo apt install python3-tk
```
## ⚙️ Installation
```bash
git clone https://github.com/FarisHotmail/IamNET.git
cd IamNET
pip install -r requirements.txt
python IamNET.py
```
## 🧭 How It Works
Internet connection is checked
Network traffic intensity is analyzed
Server list is generated
Servers are tested sequentially
Results are written to CSV files
Real-time speed is displayed via the GUI

## 🖥️ CLI Mode
CLI Parameters
Parameter	Short	Description
| File | Description |
|------|-------------|
| `--cli` | | `Enable CLI mode` |
| `--count` `-c` | `Number of servers (2–100)` |
| `--loop	-l` | `Infinite test loop` |
| `--no-traffic	–` | `Skip traffic check` |
| `--dir	-d` | `Custom save directory` |
| `--verbose	-v` | `Detailed server output` |

Background Execution (Linux)
```bash
nohup python IamNET.py --cli --loop > test.log 2>&1 &
```
CLI Examples
```bash
python IamNET.py --cli
python IamNET.py --cli --count 20
python IamNET.py --cli -c 15 -l -v
```
CLI Color Guide (Summary)
-- 🟢 Green: Success / Normal
-- 🟡 Yellow: Warning
-- 🔴 Red: Error / Critical
-- 🔵 Blue: Information
-- 🟣 Purple: Verbose details

## 📸 Screenshots
### Dashboard
![Dashboard](screenshots/dashboard.png)
### Settings
![Settings](screenshots/settings.png)

❓ FAQ
Does IamNET use speedtest.net?
→ No. Server information is retrieved from Speedtest infrastructure, but tests are performed via manual downloads.

Why do results differ?
→ Due to server location, real-time traffic, and routing variability.

Does it work with VPN?
→ Yes, but results will reflect the VPN connection speed.

🤝 Contributing
Pull Requests and Issues are welcome. For major changes, please open an issue first.

📜 License
MIT License
