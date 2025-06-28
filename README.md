# 🛡️ Threat Intelligence Harvester

Threat Intelligence Harvester is a Python-based tool that loads IOCs from a file, enriches them with GeoIP and Abuse data, and displays them in a Flask-powered dashboard with search and filtering.

## 🚀 Features

- IOC ingestion (IP, domain, hashes)
- GeoIP enrichment using MaxMind
- Abuse intelligence scoring
- Search and filter by type, value, threat type, location, and abuse score
- Beautiful CLI output with Rich + Tabulate
- Web dashboard built with Flask
- Export IOC data to JSON (WIP)
- Dockerized for deployment

## 📁 Project Structure
threat-harvester/
├── dashboard/
│   ├── app.py
│   ├── enriched_iocs.json
│   ├── templates/
│   │   └── stats.html
│   └── static/
├── exporter.py
├── GeoLite2-City.mmdb
├── harvester/
├── iocs.txt
├── main.py
├── requirements.txt
├── utils.py
├── .gitignore
├── Dockerfile
└── README.md


## 🐳 Deploy with Docker

```bash
# Build the container
sudo docker build -t threat-harvester .

# Run it
sudo docker run -p 5000:5000 threat-harvester


## 🔧 Requirements
 • Python 3.10+
 • Flask
 • geoip2
 • requests
 • rich
 • tabulate

## Screenshots

app.py.png               enriched_iocs.json.png   localhost_URL.png     requirements.txt.png           searchbox.png
 dashboard_homepage.png   IOC_table.png           'project folder.png'   running_requirements.txt.png

## 👨‍💻 Author

Reinhard Amoah
Cybersecurity Enthusiast | Threat Hunter | Python Dev
GitHub: Reinhard1268 (https://github.com/Reinhard1268)
