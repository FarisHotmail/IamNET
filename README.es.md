<p align="right">
  <a href="README.tr.md">Türkçe</a> | 
  <a href="README.en.md">English</a> | 
  <a href="README.de.md">Deutsch</a> | 
  <a href="README.fr.md">Français</a> | 
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

IamNET es una aplicación de escritorio enfocada en la privacidad, diseñada para medir la velocidad de Internet utilizando múltiples servidores nacionales e internacionales, y que funciona completamente de forma local.

🚀 Características

Pruebas de velocidad con múltiples servidores  

Separación entre servidores nacionales e internacionales  

Interfaz gráfica (basada en CustomTkinter)  

Detección de congestión de tráfico  

Soporte de salida en formato CSV  

Infraestructura multilingüe (TR / EN disponible)  

Sin telemetría  

Sin transmisión de datos  

🔐 Política de Privacidad (Importante)

IamNET:

No recopila datos del usuario  

No transmite datos  

No reporta información a sistemas externos  

No almacena ningún dato personal específico del servidor  

Archivos almacenados localmente:
Archivo | Descripción
--- | ---
yurtici_sonuclari.csv | Resultados de pruebas de servidores nacionales
yurtdisi_sonuclari.csv | Resultados de pruebas de servidores internacionales
config.json | Configuración de la aplicación

Todos los archivos se almacenan en el directorio local del usuario.

🖥️ Requisitos del Sistema

Python 3.14.2  

Windows 10 / 11  

Linux: No probado oficialmente, pero se espera que funcione  

Para Linux:

sudo apt install python3-tk

⚙️ Instalación
git clone https://github.com/FarisHotmail/IamNET.git
cd IamNET
pip install -r requirements.txt
python IamNET.py

🧭 ¿Cómo Funciona?

Se verifica la conexión a Internet  

Se analiza la intensidad del tráfico  

Se genera la lista de servidores  

Los servidores se prueban secuencialmente  

Los resultados se guardan en archivos CSV  

La velocidad instantánea se muestra a través de la GUI  

📸 Capturas de Pantalla
![Dashboard](screenshots/dashboard.png)
![Settings](screenshots/settings.png)

🛠️ Funcionalidades Planificadas

Versión CLI (línea de comandos)  

Distribución de Windows en formato .exe  

Soporte para más idiomas  

Historial de velocidad basado en gráficos  

❓ Preguntas Frecuentes

¿IamNET utiliza speedtest.net?  
→ No. La información de los servidores se obtiene de la infraestructura de Speedtest, pero las pruebas se realizan mediante descargas manuales.

¿Por qué los resultados pueden variar?  
→ Debido a la ubicación del servidor, el tráfico en tiempo real y la variabilidad de las rutas de red.

¿Funciona con VPN?  
→ Sí, pero los resultados reflejarán la velocidad de la VPN.

🤝 Contribuciones

Pull Requests e Issues están abiertos.  
Para cambios importantes, se recomienda abrir primero un Issue.

📜 Licencia

Licencia MIT