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
3. **Créez un environnement virtuel** (fortement recommandé) :
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

Avant de démarrer l'application, vous pouvez personnaliser certains aspects du projet, tels que le thème de l'application Streamlit. Pour ce faire, modifiez le fichier `.streamlit/config.toml` afin de définir les couleurs, les polices, et d'autres aspects du design.

## Structure du Projet

Voici l'arborescence des fichiers du projet :

```
COURS_STREAMLIT_IA/
│
├── .venv/
├── app/
│   ├── __init__.py
│   ├── add_cours.py
│   ├── manage_categories.py
│   ├── view_cours.py
├── data/
│   ├── cours/
│   ├── metadata.json
├── utils/
│   ├── __init__.py
│   ├── file_operations.py
│   ├── markdown_renderer.py
│   ├── metadata_operations.py
├── main.py
├── ReadMe.md
└── requirements.txt
```

### Description des Fichiers Importants
- **app/** : Contient les modules principaux pour ajouter, afficher et gérer les cours.
- **data/** : Stocke les données des cours et les métadonnées associées.
- **utils/** : Contient des fonctions utilitaires pour la manipulation des fichiers, le rendu Markdown, et la gestion des métadonnées.
- **main.py** : Point d'entrée de l'application Streamlit.
- **requirements.txt** : Liste des dépendances requises pour l'application.

## Fonctionnalités

### Page d'Accueil
La **page d'accueil** est la première page visible après le lancement de l'application. Elle propose une brève introduction à l'application, les fonctionnalités disponibles, et guide l'utilisateur pour l'utilisation de la navigation.

- **Accès** : Cette page est accessible via la barre de navigation latérale en sélectionnant "🏠 Accueil".
- **Contenu** : Message de bienvenue, description de l'application, image de présentation.

### Ajouter un Cours
La page **Ajouter un Cours** permet d'ajouter un nouveau cours à la base de données. L'utilisateur peut renseigner les informations suivantes :
- **Titre du cours**
- **Catégorie**
- **Contenu du cours** (en utilisant le Markdown pour la mise en forme)

- **Accès** : Sélectionnez "📘 Ajouter un cours" dans la barre de navigation.
- **Fonctionnalité** : Remplissez le formulaire, puis cliquez sur "Ajouter" pour enregistrer le cours.

### Voir les Cours
La page **Voir les Cours** affiche une liste de tous les cours disponibles, organisés par catégories.

- **Filtrer par Catégorie** : Un menu déroulant permet de filtrer les cours selon leur catégorie.
- **Affichage sous forme de Cartes** : Chaque cours est affiché sous forme de **carte** avec un titre, une image, et une description. Cliquez sur un bouton pour ouvrir le cours en plein écran.

- **Accès** : Sélectionnez "📚 Voir les cours" dans la barre de navigation.

### Gérer les Catégories
La page **Gérer les Catégories** permet d'ajouter, de modifier, ou de supprimer des catégories de cours.

- **Accès** : Sélectionnez "🗂️ Gérer les catégories" dans la barre de navigation.
- **Fonctionnalité** : Modifiez la liste des catégories selon les besoins des cours.

## Contribution

Si vous souhaitez contribuer à l'application, suivez les étapes ci-dessous :

1. **Forkez** le projet sur GitHub.
2. **Clonez** votre fork sur votre machine locale.
3. Créez une **branche** pour vos modifications :
   ```bash
   git checkout -b ma-branche
   ```
4. **Commitez** vos modifications :
   ```bash
   git commit -am "Ajout d'une nouvelle fonctionnalité"
   ```
5. **Poussez** votre branche :
   ```bash
   git push origin ma-branche
   ```
6. **Ouvrez une Pull Request** sur le dépôt principal pour soumettre vos modifications.

## Déploiement

Pour déployer cette application en ligne, vous pouvez utiliser **Streamlit Cloud** ou d'autres plateformes comme **Heroku** ou **AWS**. Pour Streamlit Cloud :
1. Connectez-vous à [Streamlit Cloud](https://streamlit.io/cloud).
2. Liez votre dépôt GitHub au projet.
3. Configurez les variables d'environnement si nécessaire.
4. Déployez l'application.

## Dépendances

Les dépendances de l'application sont spécifiées dans `requirements.txt`. Voici quelques-unes des bibliothèques clés :
- **Streamlit** : Pour l'interface utilisateur.
- **markdown2** : Pour le rendu Markdown.
- **watchdog** : Utilisé pour surveiller les modifications dans les fichiers (si nécessaire).

Pour installer toutes les dépendances :
```bash
pip install -r requirements.txt
```

---

Merci d'utiliser **Cours Streamlit IA** ! N'hésitez pas à nous faire part de vos commentaires et suggestions pour améliorer l'application. 😊