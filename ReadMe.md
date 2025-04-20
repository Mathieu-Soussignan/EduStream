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

### 4. Créer un fichier `.env`
Crée un fichier `.env` à la racine du projet et colle ceci :
```env
SUPABASE_URL=https://...supabase.co
SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_ROLE_KEY=eyJ...
```
Ces infos sont disponibles dans l’onglet **API > Settings** de ton projet Supabase.

### 5. Lancement de l’application
```bash
streamlit run main.py
```
> L’application s’ouvre dans [http://localhost:8501](http://localhost:8501)

---

## 🐳 Utilisation avec Docker

### 1. Lancement avec Docker Compose
```bash
docker-compose up --build
```

> Accès à l’app : [http://localhost:8501](http://localhost:8501)

### 2. Variables d’environnement
Les variables d’environnement `.env` sont automatiquement prises en compte.

### 3. Données persistées
- Les **cours** sont stockés dans Supabase (table `courses`).
- Les **profils utilisateurs** sont dans la table `profiles`.
- Les **avatars** sont sauvegardés dans le bucket `avatars` de Supabase Storage.

---

## 📂 Structure du projet

```
edustream/
├── .github/                     # github workflows
│   ├── workflows/
│   │   └── ci.yml
├── app/                       # Pages principales Streamlit
│   ├── add_cours.py
│   ├── auth_supabase.py
│   ├── login_page.py
│   ├── manage_categories.py
│   ├── profile_page.py
│   ├── view_cours.py
├── assets/                    # Visuels de l’app
│   │   └── home_ai.jpg
├── data/                     # Données des cours
├── tests/                     # Tests unitaires (pytest)
├── utils/                     # Clients Supabase et fonctions utilitaires
│   ├── file_operations.py
│   └── ia_summary_agent.py
│   └── ia_summary_utils.py
│   └── markdown_renderer.py
│   ├── metadata_operations.py
│   ├── supabase_client.py
│   ├── supabase_operations.py
├── .env                       # Clés Supabase
├── main.py                    # Point d’entrée Streamlit
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .streamlit/
    └── config.toml            # Thème & config UI Streamlit
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

## ✨ Fonctionnalités principales

### 🔐 Authentification (Supabase)
- Inscription / Connexion par email
- Authentification via JWT Supabase
- Gestion de session sécurisée avec `st.session_state`

### 📘 Ajout de cours
- Éditeur Markdown avec preview live
- Sélection de catégorie + nom de l’auteur
- Enregistrement dans Supabase (`courses`)

### 📚 Voir les cours
- Liste triable et filtrable
- Vue détaillée + bouton de modification

### 🗂️ Gestion des catégories
- Ajout / suppression de catégories globales

### 👤 Profil collaborateur
- Modification de son `display_name`, `bio`, lien GitHub
- Upload avatar personnalisé (Supabase Storage)
- Avatar visible automatiquement dans la **sidebar**

### 🤖 Résumé IA (facultatif)
- Génération automatique de résumé via modèle `distilbart-cnn-12-6`
- Bouton intégré dans la page cours

...

## 🧪 Tests & couverture

- 📁 `tests/` contient des tests unitaires pour :
  - Chargement de la config Supabase
  - Création des clients (`anon` et `service`)
  - Fonction `get_profile()`
- ✅ Compatible `pytest`

```bash
pytest
```
---

## ☁️ Déploiement

### 🌌 Compatible avec :
- Streamlit Cloud
- Render / Railway / Heroku
- Docker

### Variables à configurer dans l’environnement :
```env
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
```

### Supabase à préparer
- Table `profiles` avec colonnes : `id`, `role`, `display_name`, `bio`, `github_url`, `avatar_url`
- Bucket public `avatars`
- Règles RLS : INSERT, UPDATE, SELECT autorisés pour `authenticated`

---

## 📦 Dépendances principales

- `streamlit`
- `supabase`
- `python-dotenv`
- `pytest`
- `uuid`
- `markdown2`
- `Pillow` (si resize avatar)

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


## 🌍 Pour aller plus loin
- Ajout de **badges de contributeurs**
- IA : **résumé automatique** de contenu de cours
- Statistiques de contribution (cours ajoutés, modifiés)

---

## 💬 Contact
Un bug, une idée ?
**Contacte-moi sur Discord** → dhahaka