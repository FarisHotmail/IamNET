<p align="right">
  <a href="README.tr.md">Türkçe</a> | 
  <a href="README.en.md">English</a> | 
  <a href="README.de.md">Deutsch</a> | 
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

### Notes sur le projet
L’ensemble du code utilisé dans ce projet a été écrit à l’aide de l’outil Google Studio AI et est réalisé exclusivement à des fins de loisir.
Bien que les mises à jour ne soient pas très fréquentes, le projet continuera à évoluer dans le temps.

🔷 IamNET

IamNET est une application de bureau axée sur la confidentialité, conçue pour mesurer la vitesse de connexion Internet à l’aide de plusieurs serveurs nationaux et internationaux, et fonctionnant entièrement en local.

🚀 Fonctionnalités

- Test de vitesse multi-serveurs
- Séparation des serveurs nationaux et internationaux
- Interface graphique (basée sur CustomTkinter)
- **Mode en ligne de commande (indépendant de l'interface graphique)**
- Détection de la charge du trafic
- Exportation CSV
- Prise en charge multilingue (TR/EN)
- Affichage coloré dans le terminal
- Arrêt sécurisé par Ctrl+C
- Aucune télémétrie
- Aucune transmission de données

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

### Moteur de test en ligne de commande

- Fonctionne indépendamment de l'interface graphique
- Tous les paramètres sont configurables via les arguments de ligne de commande
- Journaux de terminal colorés et lisibles
- Interruption sécurisée avec Ctrl+C
- Convient à l'exécution en arrière-plan et à l'automatisation

### Paramètres de l'interface de ligne de commande

| Paramètre | Court | Description |
|---------|------|-------------|
| --cli | - | Activer le mode CLI |
| --count | -c | Nombre de serveurs (2–100) |
| --loop | -l | Boucle de test infinie |
| --no-traffic | - | Ignorer la vérification du trafic |
| --dir | -d | Répertoire d'enregistrement personnalisé |
| --verbose | -v | Sortie détaillée du serveur |

### Exécution en arrière-plan (Linux)
Exécuter en arrière-plan :
nohup python IamNET.py --cli --loop > test.log 2>&1 &
Test planifié (crontab) :

# Exécuter chaque nuit à 02:00
0 2 * * * /usr/bin/python3 /chemin/vers/IamNET.py --cli -c 30

🖥️ Utilisation de l'interface de ligne de commande (CLI)

Test CLI basique :
python IamNET.py --cli

Test avec 20 serveurs :
python IamNET.py --cli --count 20

Boucle infinie :
python IamNET.py --cli --loop

Ignorer la vérification du trafic :
python IamNET.py --cli --no-traffic

Sortie détaillée :
python IamNET.py --cli --verbose

Répertoire d'enregistrement personnalisé :
python IamNET.py --cli --dir /chemin/vers/dossier

Utilisation combinée :
python IamNET.py --cli -c 15 -l -v

📸 Captures d'écran (GUI)
## Tableau de bord
![Dashboard](screenshots/dashboard.png)
## Paramètres
![Settings](screenshots/settings.png)

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