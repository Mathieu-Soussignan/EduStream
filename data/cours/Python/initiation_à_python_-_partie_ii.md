
Cette deuxième partie de l'initiation à Python couvre les **bonnes pratiques** pour améliorer la qualité de votre code, notamment les fonctions, l'importation de bibliothèques, les règles de codage, ainsi que des exercices pour renforcer vos compétences. Cette partie vous guidera également sur la structuration de vos projets et sur l'utilisation de plateformes en ligne pour apprendre et pratiquer vos compétences en programmation.

## Les Bonnes Pratiques en Python

### 1. Fonctions en Python

Une fonction est définie avec le mot-clé `def`. Voici un exemple de définition de fonction :

```python
def nom_fonction(arguments, argument_defini=valeur):
    # Instructions
    return resultat1, resultat2
```

- Les arguments par défaut doivent être placés **après** les arguments non définis.
- Une fonction peut renvoyer plusieurs valeurs, qui peuvent être capturées dans une liste ou des variables séparées.

Exemple :

```python
out1, out2 = nom_fonction(arguments, argument_defini=0)
```

Dans cet exemple, `out1` et `out2` reçoivent les résultats de la fonction. Cela permet d'optimiser l'utilisation des ressources et de rendre le code plus propre.

#### Typage des Fonctions

Il est possible de typer les arguments d'une fonction ainsi que sa valeur de retour. Cela rend le code plus explicite et plus lisible, aidant ainsi les développeurs à comprendre rapidement les types de données attendus :

```python
def function(n: int) -> int:
    if n < 2:
        return 1
```

Ce typage est particulièrement utile lorsque vous travaillez en équipe, car il améliore la documentation automatique et réduit les erreurs potentielles dues à une mauvaise utilisation des arguments.

#### Fonction en une ligne

Une fonction peut être écrite en une seule ligne pour plus de concision, en particulier lorsque la logique est simple :

```python
def f(x, y): return 2 * (x + y)
```

Cela permet d'écrire des scripts plus compacts, utiles dans des cas où la lisibilité n'est pas compromise.

### 2. Fonctions dans des Fonctions

On peut créer des fonctions imbriquées lorsque leur usage est limité à la fonction externe. Cela permet de bien organiser le code et d'éviter la pollution de l'espace de noms :

```python
def function(n, a=5):
    def calcul(n, a):
        return n * a
    return calcul(n, a)
```

Les fonctions imbriquées sont particulièrement utiles lorsque vous avez besoin de tâches auxiliaires qui ne seront jamais réutilisées ailleurs dans le programme. Elles aident à garder le code plus modulaire et lisible.

### 3. Fonction Récursive

Une **fonction récursive** est une fonction qui s'appelle elle-même jusqu'à ce qu'une condition soit remplie. Par exemple, la fonction factorielle :

```python
def factorielle(n):
    return n * factorielle(n - 1) if n > 1 else 1
```

Les fonctions récursives sont utiles pour résoudre des problèmes qui peuvent être décomposés en sous-problèmes similaires. Toutefois, il est important de bien gérer la condition d'arrêt pour éviter des boucles infinies et des erreurs de dépassement de pile.

## Importer des Bibliothèques

L'importation de bibliothèques permet de réutiliser du code existant et d'enrichir vos scripts Python avec des fonctionnalités avancées.

### Importer une Bibliothèque

Pour importer une bibliothèque entière :

```python
import os
file_path = os.path.join("path", "file_name")
```

Cela permet d'accéder à toutes les fonctionnalités de la bibliothèque. Par exemple, `os` est une bibliothèque qui offre des fonctions pour interagir avec le système d'exploitation, telles que la gestion des fichiers et des répertoires.

### Importer des Fonctions Particulières

Pour économiser de la mémoire, on peut importer uniquement certaines fonctions spécifiques d'une bibliothèque :

```python
from os.path import join, isdir
if isdir("path"):
    file_path = join("path", "file_name")
```

Cette méthode est particulièrement utile lorsque vous ne souhaitez utiliser que quelques fonctions d'une bibliothèque volumineuse, réduisant ainsi l'utilisation de la mémoire.

### Importer avec un Alias

Pour simplifier l'utilisation des bibliothèques, on peut utiliser des alias. Cela est souvent fait pour des bibliothèques populaires :

```python
import numpy as np
import pandas as pd
```

Quelques bibliothèques courantes :

- **NumPy** (`import numpy as np`) : Pour les calculs numériques. Elle permet de travailler efficacement avec des tableaux multidimensionnels.
- **Matplotlib** (`import matplotlib.pyplot as plt`) : Pour l'affichage graphique. Utile pour créer des graphiques, des histogrammes, et visualiser les données.
- **Pandas** (`import pandas as pd`) : Pour manipuler des DataFrames, qui sont des structures de données tabulaires très utiles pour l'analyse de données.
- **Scikit-Learn** (`import sklearn as sk`) : Pour le Machine Learning, offrant de nombreux algorithmes prêts à l'emploi pour l'apprentissage automatique.
- **Seaborn** (`import seaborn as sns`) : Pour des visualisations de données statistiques, rendant les graphiques plus attrayants et informatifs.

## Règles de Codage

Respecter les règles de codage permet d'écrire du code maintenable, lisible, et réutilisable. Voici quelques bonnes pratiques :

1. **Déclaration des Bibliothèques** : Toujours déclarer les bibliothèques et le code personnalisé au début d'un script. Cela rend le script plus organisé et plus facile à lire.
2. **Éviter les Variables Globales** : Utiliser des variables locales autant que possible pour éviter des effets de bord indésirables et rendre le code plus modulaire.
3. **Définir les Fonctions** : Créer des fonctions pour modulariser le code. Chaque fonction doit idéalement remplir une seule tâche clairement définie.
4. **Tests Unitaires** : Tester chaque fonction de manière isolée pour garantir son bon fonctionnement avant de l'intégrer au reste du programme. Cela facilite la détection des bugs et assure une meilleure qualité du code.

### Structure d'un Projet Python

Il est recommandé de structurer votre projet de manière organisée pour faciliter la maintenance et la réutilisation du code. Voici un exemple de structure de projet :

```
Dossier App:
---- codes_folder
---- results_folder
---- statics
```

Les fichiers annexes sont placés dans des sous-dossiers, et le code principal peut importer des fonctions de ces sous-dossiers. Une bonne organisation permet de mieux s'y retrouver, notamment dans les projets de grande envergure.

## Commentaires et Documentation

Les commentaires et la documentation sont essentiels pour rendre votre code compréhensible par les autres développeurs (et par vous-même plus tard).

- Les **commentaires** commencent par `#` et permettent d'expliquer ce que fait une ligne ou un bloc de code.
- Les **sections** dans un script peuvent être démarquées par `#%%` pour être exécutées séparément dans des environnements tels que **Jupyter Notebook**. Cela facilite l'expérimentation et le développement itératif.

### Documentation d'une Fonction

Une fonction peut être documentée directement avec une chaîne de caractères juste après la définition. C'est ce qu'on appelle un **docstring** :

```python
def function(n, a=5):
    """
    Cette fonction retourne le produit de n et a.
    [n]: int, float ou array
    [a]: int, float ou array -- valeur par défaut = 5
    """
    return n * a
```

Le docstring permet d'expliquer le rôle de la fonction, les paramètres attendus, et la valeur de retour. Cela est particulièrement utile pour l'auto-documentation et pour faciliter la prise en main par d'autres développeurs.

## Google Colab

**Google Colab** est un environnement Jupyter Notebook fourni par Google. Il permet d'exécuter du code Python en ligne, gratuitement, avec des ressources de calcul fournies par Google. Vous pouvez vous connecter avec votre compte Google et tester vos codes directement.

Google Colab est particulièrement utile pour ceux qui n'ont pas de machine puissante, car il permet d'exécuter des calculs lourds sur les serveurs de Google. Vous pouvez également partager facilement vos notebooks avec d'autres personnes.

Lien : [Google Colab](https://colab.research.google.com/)

## Exercices Pratiques

Pour renforcer vos compétences en Python, il est important de pratiquer. Voici quelques idées d'exercices pratiques utilisant des fonctions de **numpy.random** pour générer des situations aléatoires :

- **Aller à l'épicerie** : Écrire un script qui modélise un achat à l'épicerie. Achetez des produits en respectant un budget maximal. Utilisez des fonctions pour chaque tâche, telles que vérifier si l'épicerie est ouverte, calculer le coût total, etc.
- **Génération aléatoire** : Utiliser `randint` pour générer des nombres aléatoires et `permutation` pour mélanger une liste d'éléments.

Ces exercices vous permettront de pratiquer l'utilisation des fonctions, des conditions, et des bibliothèques. Ils sont également un bon moyen de comprendre la logique de la programmation et de s'habituer à la résolution de problèmes.

```python
from numpy.random import randint, permutation
```

## Plateforme Code In Game

Pour améliorer vos compétences en programmation, vous pouvez utiliser **Code In Game**, une plateforme gratuite où vous pouvez participer à des challenges, apprendre de nouvelles techniques, et montrer vos accomplissements sur votre CV. La plateforme propose des défis dans différents langages de programmation, et c'est un excellent moyen d'apprendre en s'amusant.

Participer à ces défis peut vous aider à améliorer votre logique, à apprendre à optimiser votre code, et à découvrir de nouvelles façons de résoudre des problèmes.

Lien : [Code In Game](https://www.codingame.com/home)

## Conclusion

Cette partie de l'initiation à Python vous a fourni des outils pour écrire du code plus propre et plus efficace en utilisant des fonctions, des bibliothèques, et en suivant des bonnes pratiques de codage. Utilisez ces connaissances pour créer des scripts modulaires, faciles à lire et à maintenir. La maîtrise de ces concepts est essentielle pour tout développeur souhaitant créer des applications robustes et maintenables.

N'oubliez pas de pratiquer régulièrement et de vous lancer des défis personnels. Cela vous aidera à renforcer vos compétences et à devenir un meilleur programmeur Python.