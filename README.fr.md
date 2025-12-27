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

IamNET est une application de bureau axée sur la confidentialité, conçue pour mesurer la vitesse de connexion Internet à l’aide de plusieurs serveurs nationaux et internationaux, et fonctionnant entièrement en local.

🚀 Fonctionnalités

Test de vitesse via plusieurs serveurs

Séparation des serveurs nationaux / internationaux

Interface graphique (basée sur CustomTkinter)

Détection de la charge du trafic réseau

Prise en charge de l’export CSV

Infrastructure multilingue (TR / EN disponibles)

Aucune télémétrie

Aucune transmission de données

🔐 Politique de confidentialité (Important)

IamNET :

Ne collecte aucune donnée utilisateur

Ne transmet aucune donnée

Ne rapporte aucune information à des systèmes externes

Ne stocke aucune donnée personnelle spécifique aux serveurs

Fichiers stockés localement :
| Fichier | Description |
|------|------|
| yurtici_sonuclari.csv | Résultats des tests des serveurs nationaux |
| yurtdisi_sonuclari.csv | Résultats des tests des serveurs internationaux |
| config.json | Paramètres de l’application |

Tous les fichiers sont stockés dans le répertoire local de l’utilisateur.

🖥️ Configuration requise

Python 3.14.2

Windows 10 / 11

Linux : non testé, mais très probablement fonctionnel

Pour Linux :

bash
sudo apt install python3-tk

⚙️ Installation

git clone https://github.com/FarisHotmail/IamNET.git
cd IamNET
pip install -r requirements.txt
python IamNET.py


🧭 Fonctionnement

La connexion Internet est vérifiée

La charge du trafic réseau est analysée

Une liste de serveurs est générée

Les serveurs sont testés séquentiellement

Les résultats sont enregistrés dans des fichiers CSV

La vitesse instantanée est affichée via l’interface graphique

📸 Captures d’écran




🛠️ Fonctionnalités prévues

Version CLI (ligne de commande)

Distribution Windows au format .exe

Prise en charge de langues supplémentaires

Historique de vitesse basé sur des graphiques

❓ Foire aux questions

IamNET utilise-t-il speedtest.net ?
→ Non. Les informations de serveurs proviennent de l’infrastructure Speedtest, mais les tests sont effectués via des téléchargements manuels.

Pourquoi les résultats varient-ils ?
→ En raison de la localisation des serveurs, du trafic instantané et des variations de routage.

Fonctionne-t-il avec un VPN ?
→ Oui, mais les résultats refléteront la vitesse du VPN.

🤝 Contribution

Les Pull Requests et Issues sont ouverts.
Pour les modifications majeures, il est recommandé d’ouvrir d’abord une Issue.

📜 Licence

Licence MIT