
## Les Fondamentaux

### Python et Jupyter
- **Python** est un langage de programmation basé sur le C. Il s'articule autour de l'utilisation de librairies spécialisées.
- **Jupyter Notebooks** permettent d'alterner entre code Python et texte Markdown, facilitant l'apprentissage.
- **Installation** : Utilisation de Python 3 via ANACONDA et Jupyter avec VSCode.

### Python vs Autres Langages
- Python fonctionne principalement avec **l'indentation** au lieu des accolades `{}`.
- Exemple de fonction :
  ```python
  def function(n):
      if n < 2:
          return 1
  ```

### Types de Données
- **Principaux types** : `int` (entier), `float` (nombre à virgule), `string` (chaîne de caractères), `bool` (True/False).
- Structures de données : **listes**, **tuples**, **dictionnaires**.

### Opérations de Base
- **Arithmétiques** : `+`, `-`, `*`, `/`, `**` (puissance), `//` (division entière), `%` (modulo).
- **Incrémentations** : `i += 1`, `i -= 1`, etc.

### Conditions
- **If/elif/else** : Permettent de contrôler le flux d'exécution selon des conditions.
  ```python
  if color == 'rouge':
      print('la couleur est rouge')
  elif color == 'verte':
      print('la couleur est verte')
  else:
      print('mauvaise couleur')
  ```
- **Switch** (Python 3.10+) : Utilisation de `match` pour simplifier plusieurs conditions.

### Boucles
- **For** : Utilisé pour itérer sur des séquences.
  ```python
  for indice in range(10):
      print(indice)
  ```
- **While** : Répète tant qu'une condition est vraie.
  ```python
  while indice < 10:
      indice += 1
  ```

### Listes, Tuples et Dictionnaires
- **Listes** : Permettent de regrouper des éléments hétérogènes.
  ```python
  maliste = [1, 'user_login', 3.1415]
  ```
- **Tuples** : Comme des listes, mais **immuables**.
  ```python
  mon_tuple = ("a", 1, 2, 3)
  ```
- **Dictionnaires** : Utilisent des **paires clé-valeur** pour structurer les données.
  ```python
  mon_dico = {'user_1': 'moi', 1: 3.1415}
  ```

### Compréhension de Liste
- Une manière **compacte et efficace** de créer des listes.
  ```python
  out = [valeur*2 for valeur in ma_liste if valeur > 0]
  ```

## Exercices Pratiques
1. **Paire ou Impaire** : Programme pour déterminer si un nombre est pair ou impair.
2. **Calculer 80%** d'un nombre, en boucle jusqu'à ce que l'utilisateur entre `0`.
3. **Liste de 10 chiffres** : Afficher les statistiques (min, max, moyenne, somme, médiane).
4. **Liste de chiffres** jusqu'à un nombre négatif, puis afficher la liste et sa longueur.
5. **Créer une liste/dictionnaire** via l'entrée utilisateur, arrêt sur `STOP`.
6. **Calculer la somme** d'une liste jusqu'à `STOP`, en utilisant une variable temporaire.

