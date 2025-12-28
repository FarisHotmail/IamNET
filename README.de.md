<p align="center">
<a href="README.tr.md">Türkisch</a> |
<a href="README.md">English</a> |
<a href="README.fr.md">Französisch</a> |
<a href="README.es.md">Spanisch</a> |
<a href="README.ru.md">Russisch</a>
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

## Projekthinweise
Der gesamte Code dieses Projekts wurde mit Google Studio AI erstellt. Dieses Projekt ist ein reines Hobbyprojekt. Es wird weiterentwickelt, jedoch nicht regelmäßig.

## Beschreibung
IamNET ist eine datenschutzorientierte Desktop-Anwendung zur Messung der Internetgeschwindigkeit mithilfe mehrerer nationaler und internationaler Server.

Sie läuft ausschließlich lokal.

## 🚀 Funktionen
- Geschwindigkeitstest auf mehreren Servern
- Trennung von nationalen und internationalen Servern
- GUI (basierend auf CustomTkinter)
- CLI-Modus (GUI-unabhängig)

- Lasterkennung
- CSV-Export
- Mehrsprachige Unterstützung (TR/EN verfügbar)
- Farbige Terminalausgabe
- Sicheres Beenden mit Strg+C
- Keine Telemetrie
- Keine Datenübertragung

## 🔐 Datenschutzrichtlinie
IamNET:

- Erfasst keine Benutzerdaten
- Überträgt keine Daten
- Speichert keine serverbezogenen personenbezogenen Daten

**Lokal gespeicherte Dateien:**

| Datei | Beschreibung |
|------|-------------|
| `yurtici_sonuclari.csv` | Testergebnisse des nationalen Servers |
| `yurtdisi_sonuclari.csv` | Testergebnisse des internationalen Servers |
| `config.json` | Anwendungseinstellungen |

## 🖥️ Systemvoraussetzungen
- Python 3.14.2
- Windows 10 / 11
- Linux (nicht offiziell getestet)

Für Linux:
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
## 🧭 Funktionsweise
Internetverbindung wird geprüft
Netzwerkverkehrsintensität wird analysiert
Serverliste wird erstellt
Server werden nacheinander getestet
Ergebnisse werden in CSV-Dateien geschrieben
Geschwindigkeit in Echtzeit wird über die GUI angezeigt

## 🖥️ CLI-Modus
CLI-Parameter
Parameter Kurzbeschreibung
| Datei | Beschreibung |

|------|-------------|

| `--cli` | | `CLI-Modus aktivieren` |

| `--count` `-c` | `Anzahl der Server (2–100)` |

| `--loop -l` | `Endlose Testschleife` |

| `--no-traffic –` | `Verkehrsprüfung überspringen` |

| `--dir -d` | `Benutzerdefiniertes Speicherverzeichnis` |

| `--verbose -v` | `Detaillierte Serverausgabe` |

Hintergrundausführung (Linux)
```bash
nohup python IamNET.py --cli --loop > test.log 2>&1 &
CLI-Beispiele
```
```bash
python IamNET.py --cli
python IamNET.py --cli --count 20
python IamNET.py --cli -c 15 -l -v
```
CLI-Farbskala (Übersicht)
* 🟢 Grün: Erfolgreich / Normal
* 🟡 Gelb: Warnung
* 🔴 Rot: Fehler / Kritisch
* 🔵 Blau: Information
* 🟣 Lila: Ausführliche Details

## 📸 Screenshots
### Dashboard
![Dashboard](screenshots/dashboard.png)
### Einstellungen
![Settings](screenshots/settings.png)

## ❓ FAQ
* Does Nutzt IamNET speedtest.net?

* → Nein. Die Serverinformationen werden von der Speedtest-Infrastruktur bezogen, die Tests werden jedoch manuell durchgeführt.

* Warum unterscheiden sich die Ergebnisse?

* → Aufgrund des Serverstandorts, des Echtzeit-Datenverkehrs und der Routing-Variabilität.

* Funktioniert es mit VPN?

* → Ja, die Ergebnisse spiegeln jedoch die VPN-Verbindungsgeschwindigkeit wider.

## 🤝 Mitwirken
Pull Requests und Issues sind willkommen. Bei größeren Änderungen bitte zuerst ein Issue erstellen.

## 📜 Lizenz
MIT-Lizenz
