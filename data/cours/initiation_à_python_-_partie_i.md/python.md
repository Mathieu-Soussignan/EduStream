## Objectif du cours
Apprendre les bases de la programmation avec Python, en utilisant des notebooks Jupyter pour une approche interactive et pédagogique. Le cours couvre les fondamentaux du langage, des structures de données de base, et des opérations essentielles.

---

## 1. Introduction à Python & Jupyter
- Python est un langage de haut niveau basé sur C.
- Utilisation recommandée : Python 3 via Anaconda.
- Environnement de travail : Notebooks Jupyter avec VS Code + plugins.
- Notebooks : alternance de code et de texte (Markdown).

## 2. Installation et outils
- Installer : Anaconda, VSCode, GitHub, GitHub Desktop.
- Utiliser `pip install nom_du_package` pour ajouter des bibliothèques.
- Créer un répertoire Git pour vos projets Python.

## 3. Markdown dans Jupyter
- `#` pour les titres, `**gras**`, `*italique*`, etc.
- Pratique pour documenter son code.

## 4. Différences Python / C
- Python utilise **l'indentation** (tabulation) au lieu des accolades `{}`.
- Exemple :
```python
def fonction(n):
    if n < 2:
        return 1
```

## 5. Types de données
- `int`, `float`, `bool`, `str`, `list`, `tuple`, `dict`
- `type(objet)` permet de connaître le type d'une variable.

## 6. Opérations de base
- Addition, soustraction, multiplication, division, modulo...
- Opérateurs de mise à jour : `+=`, `-=`, `*=`, `/=`

## 7. Conditions
- `if`, `elif`, `else`
- Égal à : `==`, Différent : `!=`, Supérieur : `>`, Inférieur : `<`
- Condition courte : `x if condition else y`
- `match/case` disponible depuis Python 3.10

## 8. Boucles
- `for i in range(...)`
- `while condition:` avec possibilité d'utiliser `break`

## 9. Listes
- Création : `ma_liste = [1, 2, "texte"]`
- Ajout : `append`, `insert`
- Suppression : `remove`, `del`
- Parcours : `for val in liste`, `enumerate`, `zip`

## 10. Tuples
- Comme les listes, mais **non modifiables** : `mon_tuple = (1, 2, 3)`

## 11. Dictionnaires
- `mon_dico = {"cle": "valeur"}`
- Utilisation de `.keys()`, `.values()`, `.items()`
- Dictionnaires imbriqués possibles

## 12. Compréhension de liste
- Exemple : `[x*2 for x in liste if x > 0]`

## 13. Chaînes de caractères
- `"texte".upper()`, `"texte".lower()`
- `"Nom : {}".format("John")`

---

## 14. Exercices recommandés
1. Déterminer si un nombre est pair ou impair.
2. Calculer 80% d'un chiffre en boucle jusqu'à zéro.
3. Liste de 10 nombres avec stats (min, max, moyenne, somme, médiane).
4. Liste stoppée par un chiffre négatif, affichage + longueur.
5. Créer dynamiquement une liste ou un dictionnaire avec des clés/valeurs.
6. Liste stoppée par "STOP" avec somme manuelle.

---

## ✨ Bonus : Générateurs
- Fonctionnent comme des listes, mais sans stockage mémoire.
- Syntaxe : parenthèses `()` au lieu de crochets `[]`.

---

> **Auteur** : A. Schutz
> **Année** : 2022