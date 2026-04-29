# 🌱 Smart Irrigation System 🚀

> Un système d'irrigation intelligent basé sur l'IoT et l'IA pour optimiser la consommation d'eau en milieu agricole.

---

## 📋 Table des Matières
* [Aperçu](#aperçu)
* [Architecture du Projet](#architecture-du-projet)
* [Technologies Utilisées](#technologies-utilisées)
* [Installation et Configuration](#installation-et-configuration)
* [Utilisation](#utilisation)

---

## 🌟 Aperçu
Ce projet permet de surveiller l'humidité du sol et la température en temps réel via des capteurs (simulés ou réels). Une **Intelligence Artificielle** analyse les données pour décider automatiquement de l'activation ou non de la pompe d'irrigation.

---

## 🏗️ Architecture du Projet
Le système est composé de trois micro-services connectés :
1.  **Backend (Flask)** : Le cerveau qui reçoit les données, les stocke en base de données et coordonne avec l'IA.
2.  **IA Service (FastAPI)** : Un service prédictif qui analyse les seuils et retourne une décision d'irrigation.
3.  **Frontend (Dashboard)** : Une interface web moderne pour visualiser les données en temps réel.
4.  **Simulateur/IoT** : Un script simulant le comportement d'un ESP32 envoyant des données via HTTP.

---

## 🛠️ Technologies Utilisées
- **Backend** : Python, Flask, Flask-CORS, Flask-SQLAlchemy
- **IA** : FastAPI, Uvicorn, Pydantic
- **Base de Données** : SQLite (Stockage local des logs)
- **Frontend** : HTML5, Tailwind CSS, JavaScript (Fetch API)
- **Versionnage** : Git & GitHub

---

## 🚀 Installation et Configuration

### 1. Cloner le projet
```bash
git clone [https://github.com/souidelain/smart-irrigation.git](https://github.com/votre-username/smart-irrigation.git)
cd smart-irrigation

2 Setup de l'environnement virtuel
python -m venv venv
.\venv\Scripts\activate




3 Installer les dépendances
pip install -r requirements.txt



!!Lancer l'IA : 
cd ia
python api_prediction.py

!!Lancer le Backend:
cd backend
python app.py

!!Lancer le Simulateur :
cd embarque
python simulator.py


![alt text](image.png)