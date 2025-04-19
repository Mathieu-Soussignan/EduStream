# 🎓 EduStream – Plateforme collaborative de cours IA

**EduStream** est une application Streamlit connectée à Supabase, pensée pour les étudiants en data et IA, afin de centraliser, partager et modifier les cours facilement.  
📚 Ajoute tes cours, consulte ceux de ta promo, gère les catégories et personnalise ton profil collaborateur, dans une interface moderne et collaborative.

---

## 🧱 Sommaire

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

### 2. Données persistées
- Les **cours** sont stockés dans Supabase (table `courses`).
- Les **profils utilisateurs** sont dans la table `profiles`.
- Les **avatars** sont sauvegardés dans le bucket `avatars` de Supabase Storage.

---

## 📂 Structure du projet

```
edustream/
├── app/
│   ├── add_cours.py              # Ajout et modification de cours
│   ├── manage_categories.py      # Gestion des catégories
│   ├── view_cours.py             # Affichage et détail des cours
│   └── profile_page.py           # Page profil collaborateur
├── utils/
│   ├── supabase_client.py        # Connexion Supabase et clients API
│   └── profile_helper.py         # Fonctions de manipulation des profils
├── tests/                        # Tests unitaires Pytest
├── assets/
│   └── home_ai.jpg               # Image d'accueil
├── .env                          # Clés Supabase locales
├── main.py                       # Entrée principale de l'app Streamlit
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .streamlit/
    └── config.toml            # Thème et config UI Streamlit
```

---

## ✨ Fonctionnalités

### 🏠 Accueil
- Vue d’introduction + image + rappel des objectifs

### 📘 Ajouter un cours
- Titre, contenu markdown, catégorie, auteur
- Aperçu live du contenu
- Sauvegarde vers Supabase

### 📚 Voir les cours
- Liste de tous les cours ajoutés par les utilisateurs
- Filtres par catégorie + recherche texte
- Accès à la fiche détaillée d’un cours
- 🔄 Possibilité de modifier le contenu d'un cours

### 🗂️ Gérer les catégories
- Ajout/suppression dynamique
- Utilisé dans le formulaire d’ajout de cours

### 👤 Profil collaborateur
- Modification du nom affiché, bio, lien GitHub
- Upload d’un avatar personnalisé (Stocké dans Supabase Storage)
- 🚀 L’avatar est affiché automatiquement dans la sidebar de l’utilisateur connecté

---

## 🧑‍💻 Contribution

1. Fork du repo
2. Crée une branche :
   ```bash
   git checkout -b feat/ma-nouvelle-fonctionnalite
   ```
3. Fait tes modifications
4. Commit :
   ```bash
   git commit -m "feat: ajout avatar dans la sidebar"
   ```
5. Push & Pull Request

---

## ☁️ Déploiement

### 🌌 Compatible avec :
- Streamlit Cloud
- Render / Railway / Heroku
- Docker

Clés à configurer dans l’environnement :
```
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
```

---

## 📦 Dépendances principales

- `streamlit`
- `supabase`
- `python-dotenv`
- `pytest`
- `uuid`
- `markdown2`

---

## 🌍 Pour aller plus loin
- Ajout de **badges de contributeurs**
- IA : **résumé automatique** de contenu de cours
- Statistiques de contribution (cours ajoutés, modifiés)

---

## 💬 Contact
Un bug, une idée ?
**Contacte-moi sur Discord** → dhahaka