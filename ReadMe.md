
# Cours Streamlit IA - Documentation

Bienvenue sur l'application **Cours Streamlit IA**, une plateforme dédiée à la gestion des cours liés à l'apprentissage automatique et à l'intelligence artificielle. Cette application permet d'ajouter des cours, de les consulter et de gérer les différentes catégories de cours de manière simple et intuitive, le tout en utilisant **Streamlit**. Voici un guide exhaustif pour comprendre comment installer, configurer, et utiliser cette application.

## Table des Matières
- [Installation](#installation)
- [Configuration Initiale](#configuration-initiale)
- [Structure du Projet](#structure-du-projet)
- [Fonctionnalités](#fonctionnalités)
  - [Page d'Accueil](#page-daccueil)
  - [Ajouter un Cours](#ajouter-un-cours)
  - [Voir les Cours](#voir-les-cours)
  - [Gérer les Catégories](#gérer-les-catégories)
- [Contribution](#contribution)
- [Déploiement](#déploiement)
- [Dépendances](#dépendances)
- [Utilisation avec Docker](#utilisation-avec-docker)
- [Fonctionnalités Récentes](#fonctionnalités-récentes)

## Installation

Pour installer et utiliser l'application **Cours Streamlit IA**, suivez les étapes ci-dessous :

1. **Clonez le dépôt GitHub** :
   ```bash
   git clone <URL_DU_DEPOT_GITHUB>
   ```
2. **Accédez au répertoire du projet** :
   ```bash
   cd cours_streamlit_IA
   ```
3. **Créez un environnement virtuel** :
   ```bash
   python -m venv .venv
   ```
4. **Activez l'environnement virtuel** :
   - Sur **Windows** :
     ```bash
     .venv\Scripts\activate
     ```
   - Sur **macOS/Linux** :
     ```bash
     source .venv/bin/activate
     ```
5. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
6. **Lancez l'application** :
   ```bash
   streamlit run main.py
   ```

## Configuration Initiale

Modifiez le fichier `.streamlit/config.toml` pour personnaliser le thème, la police et l'affichage global de l'application. Le thème par défaut est en dark mode avec une interface large.

## Structure du Projet

```
cours_streamlit_IA/
├── app/
│   ├── add_cours.py
│   ├── manage_categories.py
│   ├── view_cours.py
├── data/
│   ├── cours/
│   ├── metadata.json
├── utils/
│   ├── file_operations.py
│   ├── markdown_renderer.py
│   ├── metadata_operations.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .streamlit/
    └── config.toml
```

## Fonctionnalités

### Page d'Accueil
Une présentation de l'application, son objectif, et un visuel illustratif.

### Ajouter un Cours
- Remplir un formulaire avec le titre, la catégorie, le contenu en Markdown, et le nom du contributeur
- Prévisualisation du contenu avant sauvegarde

### Voir les Cours
- Affichage sous forme de cartes avec filtres par catégorie et recherche par mot-clé
- Accès au détail du cours avec un bouton pour le modifier

### Gérer les Catégories
- Ajouter ou supprimer des catégories manuellement

## Contribution

1. Fork du projet
2. Nouvelle branche
3. Commit
4. Pull request

## Déploiement

L'application peut être déployée sur :
- **Streamlit Cloud**
- **Docker** via `docker-compose`
- **Heroku**, **Render**, etc.

---

## Dépendances

Les principales :
- `streamlit`
- `markdown2`
- `watchdog`

---

## Utilisation avec Docker

### 1. Prérequis
- Docker installé

### 2. Lancer l'application
```bash
docker-compose up --build
```

- Accès sur : [http://localhost:8501](http://localhost:8501)
- Les données sont **persistées** localement dans le dossier `./data`

---

## Fonctionnalités Récentes

- 🔍 Recherche par mot-clé dans les titres de cours
- 📄 Aperçu avant publication
- ✏️ Modification des cours
- 💾 Persistance des données avec Docker
- 🌑 Dark mode + layout large
- 🐳 Dockerisation complète et prête à l’emploi