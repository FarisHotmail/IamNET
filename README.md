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

### Project Notes
All code used in this project was written using the Google Studio AI tool and is intended purely as a hobby project.
Although not very frequently, the project will continue to be developed over time.

🔷 IamNET

IamNET is a desktop application designed to measure internet speed using multiple domestic and international servers.  
It operates entirely locally and is focused on user privacy.

🚀 Features

- Multi-server speed testing
- Domestic / international server separation
- GUI (CustomTkinter-based)
- **CLI mode (GUI-independent)**
- Traffic load detection
- CSV export
- Multi-language support (TR / EN ready)
- Colored terminal output
- Ctrl+C safe stop
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

### CLI Test Engine

- Runs completely independent from GUI
- All settings configurable via command-line arguments
- Colored and readable terminal logs
- Safe interruption with Ctrl+C
- Suitable for background execution and automation

### CLI Parameters

| Parameter | Short | Description |
|---------|------|-------------|
| --cli | - | Enable CLI mode |
| --count | -c | Number of servers (2–100) |
| --loop | -l | Infinite test loop |
| --no-traffic | - | Skip traffic check |
| --dir | -d | Custom save directory |
| --verbose | -v | Detailed server output |

### Background Execution (Linux)
Run in background:
nohup python IamNET.py --cli --loop > test.log 2>&1 &

Scheduled test (crontab):
# Run every night at 02:00
0 2 * * * /usr/bin/python3 /path/to/IamNET.py --cli -c 30

🖥️ CLI Usage

Basic CLI test:
python IamNET.py --cli

Test with 20 servers:
python IamNET.py --cli --count 20

Infinite loop:
python IamNET.py --cli --loop

Skip traffic check:
python IamNET.py --cli --no-traffic

Verbose output:
python IamNET.py --cli --verbose

Custom save directory:
python IamNET.py --cli --dir /path/to/folder

Combined usage:
python IamNET.py --cli -c 15 -l -v

📸 Screenshots (GUI)
## Dashboard
![Dashboard](screenshots/dashboard.png)
## Settings
![Settings](screenshots/settings.png)

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