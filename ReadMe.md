# 🎓 EduStream – Plateforme collaborative de cours IA

**EduStream** est une application Streamlit pensée pour les étudiants en data et IA, afin de centraliser, partager et modifier les cours facilement.  
📚 Ajoute tes cours, consulte ceux de ta promo, gère les catégories, le tout dans une interface moderne et collaborative.

---

## 🧭 Sommaire

- [🚀 Installation locale](#-installation-locale)
- [🐳 Utilisation avec Docker](#-utilisation-avec-docker)
- [📂 Structure du projet](#-structure-du-projet)
- [✨ Fonctionnalités](#-fonctionnalités)
- [🧑‍💻 Contribution](#-contribution)
- [☁️ Déploiement](#-déploiement)
- [📦 Dépendances](#-dépendances)

---

## 🚀 Installation locale

### 1. Clone du repo
```bash
git clone https://github.com/TON_USER/edustream.git
cd edustream
```

### 2. Création de l'environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
```

### 3. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancement de l’application
```bash
streamlit run main.py
```

---

## 🐳 Utilisation avec Docker

### 1. Lancement avec Docker Compose
```bash
docker-compose up --build
```

> Accès à l’app : [http://localhost:8501](http://localhost:8501)

### 2. Où sont stockées les données ?
Tous les cours et fichiers sont persistés dans le dossier local `./data`.

---

## 📂 Structure du projet

```
edustream/
├── app/
│   ├── add_cours.py              # Ajout et modification de cours
│   ├── manage_categories.py      # Gestion des catégories
│   ├── view_cours.py             # Affichage et filtrage des cours
│   └── auth.py                   # (En option) Authentification Supabase
├── utils/
│   ├── file_operations.py        # Lecture/écriture fichiers cours
│   ├── metadata_operations.py    # Manipulation des métadonnées
│   └── markdown_renderer.py      # Rendu du markdown
├── data/
│   ├── cours/                    # Contenu des cours (fichiers Markdown)
│   └── metadata.json             # Infos sur chaque cours
├── assets/
│   └── home_ai.jpg               # Image d'accueil
├── main.py                       # Point d’entrée de l’application
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .streamlit/
    └── config.toml               # Thème et config globale
```

---

## ✨ Fonctionnalités

### 🏠 Page d’Accueil
- Vue d’introduction
- Objectif de la plateforme
- Image illustrative

### 📘 Ajouter un cours
- Formulaire avec :
  - Titre
  - Catégorie
  - Contenu en Markdown
  - Nom/email du contributeur
- ✅ **Aperçu en temps réel**
- 📅 Sauvegarde automatique du fichier et des métadonnées

### 📚 Voir les cours
- 🔎 **Recherche par mot-clé**
- 📁 Filtrage par catégorie
- 📄 Accès aux détails d’un cours
- ✏️ **Bouton de modification rapide**

### 🗂️ Gérer les catégories
- Ajout/suppression de catégories utilisées pour organiser les cours

---

## 🧑‍💻 Contribution

### Étapes pour contribuer :
1. Fork du repo
2. Création d’une branche :
   ```bash
   git checkout -b ma-branche
   ```
3. Commit :
   ```bash
   git commit -m "✨ Ajout fonctionnalité de recherche"
   ```
4. Push :
   ```bash
   git push origin ma-branche
   ```
5. Ouvre une **Pull Request**

---

## ☁️ Déploiement

L'application peut être facilement déployée via :
- **Streamlit Community Cloud**
- **Render / Heroku / Railway**
- **Docker (recommandé pour usage local collaboratif)**

---

## 📦 Dépendances principales

- `streamlit` – UI simple et interactive
- `markdown2` – Rendu Markdown
- `watchdog` – Suivi de fichiers (facultatif)
- `python-dotenv` – Chargement des variables d’environnement

---

## 🚧 Fonctionnalités prévues / à réactiver
- 🔐 Authentification via Supabase (GitHub / Email)
- 🤖 Résumé automatique avec IA
- 👤 Page profil collaborateur

---

## 💬 Contact
Tu veux proposer des idées ou aider à améliorer l’app ?  
**Ping moi sur Discord !** 👉 _@mathieu_