
Dans cette troisième partie de l'initiation à Python, nous abordons la **programmation orientée objet (POO)**. La POO est une façon de structurer le code qui améliore la qualité, la lisibilité, et la modularité des projets en créant des objets qui interagissent entre eux. Voici un aperçu des concepts fondamentaux de la POO, tels que l'héritage, l'encapsulation, et les accesseurs/mutateurs.

## Programmation Orientée Objet (POO)
La programmation orientée objet permet de créer des **objets** qui ont leurs propres attributs et méthodes. Un objet est une instance d'une **classe**, et une classe est un modèle qui définit les caractéristiques de cet objet.

La POO aide à créer un code plus clair et mieux organisé. Par exemple, une classe peut être complexe à construire au début, mais une fois définie, elle permet de simplifier la réutilisation et la maintenance du code.

### Définir une Classe
Pour définir une classe, on utilise le mot-clé `class` :

```python
class MaClass_1:
    """
    Une classe simple en Python.
    """
    pass
```

Pour créer une instance de cette classe :

```python
instance_de_ma_classe = MaClass_1()
```

### Attributs et Méthodes d'une Classe
Les **attributs** sont des variables qui décrivent les caractéristiques de l'objet, tandis que les **méthodes** sont des fonctions qui définissent le comportement de l'objet.

```python
class MaClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def affiche(self):
        print(self.a, self.b, self.c)

    def __str__(self):
        return "Ma classe ou autre chose"
```
- `__init__` est un **constructeur** appelé lors de la création de l'objet. Il initialise les attributs.
- `__str__` est une méthode spéciale qui définit comment l'objet doit être affiché lorsqu'on utilise `print()`.
- `self` fait référence à l'instance courante de la classe.

## Le Concept d'Héritage
L'**héritage** permet de créer une nouvelle classe qui hérite des attributs et méthodes d'une classe existante. Cela permet de réutiliser le code et de le spécialiser.

Par exemple, une classe `Personnage` peut être la classe de base pour des classes spécifiques comme `Guerrier` et `Magicien`.

```python
class Personnage:
    def __init__(self, age, taille, poids, HP=100):
        self.age = age
        self.taille = taille
        self.poids = poids
        self.HP = HP

    def __str__(self):
        return "Personnage"

class Guerrier(Personnage):
    def __init__(self, age, taille, poids, force):
        super().__init__(age, taille, poids)
        self.force = force

    def attaque(self, ennemi):
        ennemi.HP -= self.force

    def __str__(self):
        return f"{super().__str__()}, Guerrier"
```
- **`super()`** permet d'appeler le constructeur de la classe parente pour initialiser les attributs hérités.
- Les classes `Guerrier` et `Magicien` héritent des attributs et méthodes de la classe `Personnage`, mais peuvent également avoir des attributs et méthodes spécifiques.

### Héritage Multiple
Python prend également en charge l'**héritage multiple**, ce qui signifie qu'une classe peut hériter de plusieurs classes.

```python
class GuerrierMage(Guerrier, Magicien):
    pass
```
Le `GuerrierMage` hérite naturellement des attributs et des méthodes des classes `Guerrier` et `Magicien`.

## Encapsulation
L'**encapsulation** est utilisée pour restreindre l'accès direct aux attributs d'une classe. Cela améliore la sécurité et l'intégrité des données.

### Exemple d'Encapsulation
Pour protéger les attributs d'une classe, on peut les déclarer comme **privés** en utilisant un double underscore (`__`) :

```python
class Personnage:
    def __init__(self, position, HP):
        self.__position = position
        self.__HP = HP

    def setHP(self, valeur):
        self.__HP = valeur
```
Dans cet exemple, `__HP` est un attribut privé qui ne peut être modifié qu'à l'intérieur de la classe. Cela empêche des modifications non désirées de l'extérieur.

## Accesseurs et Mutateurs
Les **accesseurs** et **mutateurs** sont des méthodes utilisées pour obtenir ou modifier les attributs privés d'une classe.

### Exemple d'Accesseurs et Mutateurs

```python
class Point:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x
```
- `get_x()` est un **accesseur** qui retourne la valeur de `__x`.
- `set_x()` est un **mutateur** qui modifie la valeur de `__x`.

### Utilisation de @property
Python permet de gérer les accesseurs et les mutateurs de manière plus élégante avec le décorateur `@property`.

```python
class Point:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
```
- Le décorateur `@property` permet d'accéder à l'attribut `_x` comme s'il s'agissait d'un attribut public.
- Le décorateur `@x.setter` permet de définir une méthode pour modifier la valeur de `_x`.

## Méthodes Magiques (Dunders)
Les **méthodes magiques** (ou **méthodes spéciales**) sont des méthodes qui commencent et se terminent par un double underscore (`__`). Elles sont aussi appelées **dunders** (de "double underscore").

### Exemples de Méthodes Magiques
- **`__init__`** : Constructeur, appelé lors de la création d'une instance.
- **`__str__`** : Définit la façon dont l'objet est représenté sous forme de chaîne de caractères.
- **`__add__`** : Permet de définir le comportement de l'opérateur `+` pour les objets de la classe.

Vous pouvez explorer de nombreuses autres méthodes magiques pour enrichir vos classes et rendre vos objets plus puissants et expressifs.

## Exercices Pratiques
Pour vous entraîner, définissez des objets et faites-les interagir, comme les personnages `Guerrier` et `Magicien`.

- **Étape 1** : Définissez une classe mère qui possède des variables et des attributs communs.
- **Étape 2** : Créez des classes qui héritent de la classe mère et ajoutez des attributs spécifiques.
- **Étape 3** : Développez des interactions entre les objets.

Par exemple, faites des combats entre des guerriers et des magiciens. Vous êtes libre de définir les règles et de rendre l'exercice amusant, même si cela implique des scénarios absurdes.

## Conclusion
La programmation orientée objet est un puissant paradigme qui permet de créer du code réutilisable, modulaire et plus facile à maintenir. En comprenant les concepts de classes, d'objets, d'héritage, d'encapsulation, et d'accesseurs/mutateurs, vous serez en mesure d'écrire des programmes Python plus robustes et sophistiqués.