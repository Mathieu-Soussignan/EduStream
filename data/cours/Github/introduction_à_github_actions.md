
**GitHub Actions** est un outil intégré à GitHub qui permet d'automatiser de nombreuses tâches liées au développement logiciel, notamment l'exécution des tests unitaires à chaque modification du code. Cet outil facilite l'intégration continue (CI) et permet de maintenir une bonne qualité de code.

## Pourquoi utiliser GitHub Actions ?

### 1. Intégration Continue (CI)
À chaque fois que vous poussez du code sur votre dépôt GitHub, **GitHub Actions** peut déclencher automatiquement vos tests. Cela permet de détecter les erreurs et les régressions rapidement, avant qu'elles ne se propagent dans votre projet.

### 2. Gain de Temps
Avec GitHub Actions, plus besoin de lancer manuellement vos tests : tout est automatisé. Cela vous permet de vous concentrer sur le développement, sans avoir à vous soucier de l'exécution régulière des tests.

### 3. Qualité du Code
En exécutant systématiquement vos tests, vous vous assurez que votre code reste fonctionnel et maintenable, même après des modifications importantes. Cela réduit les risques de bugs et facilite le processus de maintenance.

### 4. Collaboration Facilitée
Les résultats des tests sont visibles directement sur GitHub, ce qui facilite la communication et la collaboration entre les membres de l'équipe. Tout le monde peut voir l'état des tests et prendre des décisions en conséquence.

## Comment Automatiser les Tests avec GitHub Actions ?

### 1. Créer un Fichier de Workflow
Pour commencer à utiliser GitHub Actions, vous devez créer un fichier de workflow. Dans votre dépôt GitHub, créez un fichier dans le répertoire **.github/workflows/**, par exemple **tests.yml**. Ce fichier définit les étapes de votre workflow d'automatisation.

### 2. Définir les Déclencheurs
Les **déclencheurs** indiquent quand vous souhaitez que le workflow soit exécuté. Par exemple, vous pouvez décider d'exécuter les tests à chaque *push* sur la branche `main` ou lors de la création d'une *pull request*.

### 3. Configurer l'Environnement
Spécifiez l'environnement d'exécution de vos tests, y compris le système d'exploitation (par exemple, Ubuntu), la version de Python, et les dépendances requises pour votre projet. Cela permet d'avoir un environnement cohérent à chaque exécution du workflow.

### 4. Exécuter les Tests
Utilisez les actions appropriées pour installer les dépendances, puis lancez vos tests avec la commande de votre framework de test (par exemple, `pytest`, `unittest`). Cette étape garantit que votre code est testé de manière systématique et fiable.

### 5. Afficher les Résultats
Les résultats des tests peuvent être affichés directement sur GitHub. Vous pouvez configurer des actions pour publier les résultats dans les commentaires des *pull requests*, offrant une vue d'ensemble claire de la qualité de la contribution.

## Exemple de Workflow pour Pytest
Voici un exemple simple de fichier de workflow pour exécuter des tests avec `pytest` :

```yaml
name: Python application CI/CD

on:
  push:
    branches: [ main, dev ]  # Branches à surveiller
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11"]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements_train.txt
        # Ajouter des commandes d'installation spécifiques
        pip install -e libcpab
    - name: Run unit tests (un fichier)
      run: |
        pytest tests/test_0.py
    - name: Run unit tests (un autre fichier)
      run: |
        pytest tests/test_1.py
```

### Explication de l'Exemple
- **Déclencheurs** : Le workflow est déclenché à chaque *push* sur les branches `main` et `dev`, ainsi qu'à chaque *pull request* vers la branche `main`.
- **Environnement** : Le workflow s'exécute sur `ubuntu-latest` et utilise Python 3.11.
- **Étapes** :
  1. **Checkout** : Récupère le code source à l'aide de `actions/checkout@v3`.
  2. **Configuration de Python** : Installe Python en utilisant `actions/setup-python@v3`.
  3. **Installation des Dépendances** : Met à jour `pip` et installe les dépendances du projet définies dans le fichier `requirements_train.txt`.
  4. **Exécution des Tests** : Exécute les tests unitaires à l'aide de `pytest` pour différents fichiers de test.

## Conclusion
GitHub Actions est un outil puissant pour l'automatisation des workflows de développement. Grâce à l'intégration continue, il permet de s'assurer que chaque modification du code est testée et valide. Cela améliore la qualité du code, facilite la collaboration entre les développeurs, et permet de gagner du temps en automatisant les tâches répétitives.