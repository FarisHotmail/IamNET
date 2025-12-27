<p align="right">
  <a href="README.tr.md">Türkçe</a> | 
  <a href="README.en.md">English</a> | 
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

### Projekt-Hinweise
Der gesamte in diesem Projekt verwendete Code wurde mit dem Tool Google Studio AI erstellt und dient ausschließlich Hobbyzwecken.
Auch wenn nicht sehr häufig, wird das Projekt im Laufe der Zeit weiterentwickelt.

🔷 IamNET

IamNET ist eine datenschutzorientierte Desktop-Anwendung, die darauf abzielt,
die Internetgeschwindigkeit über mehrere nationale und internationale Server zu messen.
Die Anwendung arbeitet vollständig lokal.

🚀 Funktionen

Geschwindigkeitstest mit mehreren Servern

Trennung zwischen nationalen und internationalen Servern

GUI (basierend auf CustomTkinter)

Erkennung hoher Netzwerkverkehrslast

CSV-Ausgabeunterstützung

Mehrsprachige Infrastruktur (TR / EN verfügbar)

Keine Telemetrie

Keine Datenübertragung

🔐 Datenschutzrichtlinie (Wichtig)

IamNET:

Erfasst keine Benutzerdaten

Überträgt keine Daten

Berichtet nicht an externe Systeme

Speichert keine server- oder benutzerspezifischen personenbezogenen Daten

Lokal gespeicherte Dateien:
Datei	Beschreibung
yurtici_sonuclari.csv	Testergebnisse nationaler Server
yurtdisi_sonuclari.csv	Testergebnisse internationaler Server
config.json	Anwendungseinstellungen

Alle Dateien werden ausschließlich im lokalen Verzeichnis des Benutzers gespeichert.

🖥️ Systemanforderungen

Python 3.14.2

Windows 10 / 11

Linux: Nicht getestet, funktioniert jedoch sehr wahrscheinlich

Für Linux:

sudo apt install python3-tk

⚙️ Installation
git clone https://github.com/FarisHotmail/IamNET.git
cd IamNET
pip install -r requirements.txt
python IamNET.py

🧭 Funktionsweise

Überprüfung der Internetverbindung

Analyse der Netzwerkverkehrslast

Erstellung der Serverliste

Sequenzielles Testen der Server

Speicherung der Ergebnisse in CSV-Dateien

Anzeige der aktuellen Geschwindigkeit über die GUI

### CLI-Test-Engine

- Läuft völlig unabhängig von der GUI
- Alle Einstellungen über Kommandozeilenargumente konfigurierbar
- Farbige und gut lesbare Terminalprotokolle
- Sicherer Abbruch mit Strg+C
- Geeignet für Hintergrundausführung und Automatisierung

### CLI-Parameter

| Parameter | Kurzbeschreibung | Beschreibung |
---------|------|-------------|
| --cli | - | CLI-Modus aktivieren |
| --count | -c | Anzahl der Server (2–100) |
| --loop | -l | Endlosschleife |
| --no-traffic | - | Verkehrsprüfung überspringen |
| --dir | -d | Benutzerdefiniertes Speicherverzeichnis |
| --verbose | -v | Ausführliche Serverausgabe |

### Hintergrundausführung (Linux)
Im Hintergrund ausführen:
nohup python IamNET.py --cli --loop > test.log 2>&1 &

Geplanter Test (Crontab):
# Jede Nacht um 02:00 Uhr ausführen
0 2 * * * /usr/bin/python3 /Pfad/zu/IamNET.py --cli -c 30

🖥️ CLI-Nutzung

Einfacher CLI-Test:
python IamNET.py --cli

Test mit 20 Servern:
python IamNET.py --cli --count 20

Endlosschleife:
python IamNET.py --cli --loop

Verkehrsprüfung überspringen:
python IamNET.py --cli --no-traffic

Ausführliche Ausgabe:
python IamNET.py --cli --verbose

Benutzerdefiniertes Speicherverzeichnis:
python IamNET.py --cli --dir /Pfad/zum/Ordner

Kombinierte Nutzung:
python IamNET.py --cli -c 15 -l -v

📸 Screenshots (GUI)
## Armaturenbrett
![Dashboard](screenshots/dashboard.png)
## Einstellungen
![Settings](screenshots/settings.png)

❓ Häufig gestellte Fragen

Verwendet IamNET speedtest.net?
→ Nein. Serverinformationen stammen aus der Speedtest-Infrastruktur, die Tests selbst erfolgen jedoch über manuelle Downloads.

Warum unterscheiden sich die Ergebnisse?
→ Serverstandort, momentane Netzwerklast und Routing-Unterschiede.

Funktioniert IamNET mit VPN?
→ Ja, allerdings spiegeln die Ergebnisse die VPN-Geschwindigkeit wider.

🤝 Mitwirken

Pull Requests und Issues sind willkommen.
Bei größeren Änderungen wird empfohlen, vorab ein Issue zu eröffnen.

📜 Lizenz

MIT License