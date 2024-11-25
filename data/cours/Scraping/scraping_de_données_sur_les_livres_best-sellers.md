Ce document est un résumé complet du code utilisé pour extraire des informations à partir de la page web "Chasse aux livres - Best-sellers". Vous trouverez des explications pas à pas sur chaque partie du code afin de comprendre comment il fonctionne et pourquoi chaque étape est importante.

#### **1. Introduction à la Récupération de Données (Scraping)**

Le scraping est une technique qui consiste à extraire des données d'une page web. Pour ce projet, nous avons utilisé Python avec les bibliothèques **requests**, **BeautifulSoup**, et **pandas** pour extraire les informations sur les livres best-sellers, telles que le **titre**, le **prix**, l'**état** (neuf ou occasion), et l'**URL de l'image**. Ces données sont ensuite organisées dans un tableau (DataFrame) pour une manipulation plus facile.

#### **2. Importation des Bibliothèques**

Pour commencer, nous avons besoin des bibliothèques suivantes :
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```
- **requests** : Envoie des requêtes HTTP pour récupérer le contenu des pages web.
- **BeautifulSoup** : Parse (analyse) le HTML de la page web pour trouver des éléments spécifiques.
- **pandas** : Crée un DataFrame pour organiser les informations sous forme de tableau.

#### **3. Structure de la Fonction `scrape_livres()`**

La fonction `scrape_livres()` a pour objectif de se connecter à la page cible, extraire les informations des livres et les renvoyer sous forme de DataFrame.

Voici les étapes principales :

##### **a) Faire une Requête GET**
```python
url = 'https://www.chasse-aux-livres.fr/best-sellers'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}
response = requests.get(url, headers=headers)
```
- **URL** : L'adresse de la page à scraper est définie.
- **Headers** : Le `user-agent` est ajouté pour simuler une requête provenant d'un vrai navigateur, permettant de contourner certaines restrictions de sites web.
- **Requête GET** : Récupération du contenu de la page.
- **Vérification du Statut** : Si le code de statut n'est pas **200** (succès), le programme s'arrête.

##### **b) Parser le Contenu de la Page**
```python
soup = BeautifulSoup(response.content, "html.parser")
livres = soup.find('tbody').find_all('tr')
```
- **BeautifulSoup** est utilisé pour analyser le HTML de la page.
- **Trouver les livres** : Le tableau contenant les informations des livres est localisé (à l'intérieur de la balise `<tbody>`), et chaque livre est identifié comme une balise `<tr>`.

##### **c) Extraction des Informations des Livres**
Pour chaque livre, nous extrayons les informations suivantes :

###### **i) Titre du Livre**
```python
titre = livre.find('p', class_="title-p").find('a').text.strip()
```
- Le titre est trouvé dans une balise `<p>` avec la classe `title-p`, qui contient un lien (`<a>`).
- Le texte est extrait et les espaces indésirables sont retirés avec `strip()`.

###### **ii) Prix et État**
```python
prix_element = livre.find('p', class_="last-price")
prix = None
etat = "Non disponible"

if prix_element:
    prix_texte = prix_element.text.strip()
    try:
        if "Neuf" in prix_texte:
            etat = "Neuf"
            prix_str = prix_texte.split("Neuf")[-1].strip()
        elif "Occasion" in prix_texte:
            etat = "Occasion"
            prix_str = prix_texte.split("Occasion")[-1].strip()
        else:
            prix_str = None

        # Convertir le prix en float
        if prix_str:
            prix = float(prix_str.replace(',', '.').replace(' €', ''))
    except ValueError:
        prix = None
```
- **État et Prix** : Le prix et l'état ("Neuf" ou "Occasion") sont extraits de la balise avec la classe `last-price`.
- **Conversion en `float`** : Le prix est converti en `float` pour permettre de futures manipulations quantitatives. Le texte est nettoyé pour enlever les espaces, la virgule est remplacée par un point, et le symbole `€` est retiré.
- **Gestion des erreurs** : En cas de problème lors de la conversion (par exemple, une valeur manquante), le prix est défini sur `None`.

###### **iii) URL de l'Image**
```python
image_element = livre.find('td', class_="cover").find('img')
image_url = image_element.get('src') if image_element and image_element.has_attr('src') else "Non disponible"
```
- **Extraction de l'image** : L'image est trouvée dans la cellule (`<td>`) avec la classe `cover`, qui contient une balise `<img>`.
- Si l'attribut `'src'` est présent, l'URL est extraite, sinon l'URL est définie à "Non disponible".

##### **d) Stocker les Informations des Livres**
```python
data.append({'Titre': titre, 'Prix': prix, 'État': etat, 'Image URL': image_url})
```
- **Liste `data`** : Chaque livre est ajouté à la liste `data` sous forme de dictionnaire contenant le titre, le prix, l'état et l'URL de l'image.

##### **e) Création du DataFrame pandas**
```python
return pd.DataFrame(data)
```
- **DataFrame** : Le tableau des informations extraites est transformé en **DataFrame pandas**, une structure très utile pour l'analyse des données.

#### **4. Appel de la Fonction et Affichage des Résultats**
```python
df_livres = scrape_livres()
print(df_livres)
```
- **Appel de la fonction** : La fonction `scrape_livres()` est appelée, et les résultats sont stockés dans `df_livres`.
- **Affichage** : Affiche le DataFrame, présentant toutes les informations des livres dans un tableau.

#### **5. Résumé et Importance**
- **Scraper les données de la page "Chasse aux livres"** nous permet d'extraire les informations des livres directement à partir de leur page best-sellers.
- Les données **structurées en DataFrame** peuvent être facilement analysées, filtrées ou utilisées pour des rapports.
- La conversion du **prix en `float`** permet d'effectuer des calculs, comme des statistiques ou des comparaisons entre les prix de plusieurs livres.