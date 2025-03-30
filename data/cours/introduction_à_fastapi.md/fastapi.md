## 🌐 Qu'est-ce que FastAPI ?
FastAPI est un framework web moderne pour créer des APIs rapides, fiables et bien documentées.

**Points forts :**
- Ultra performant (comme Node.js ou Go)
- Documentation interactive automatique (Swagger UI)
- Validation native des données via **Pydantic**

---

## 📖 Installation rapide
```bash
pip install fastapi uvicorn
```

Fichier `main.py` :
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Lancer le serveur :
```bash
uvicorn main:app --reload
```

---

## 📚 Les routes (endpoints)
Chaque route correspond à une URL et une méthode HTTP (GET, POST, etc).
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

---

## 📈 Validation avec Pydantic
FastAPI utilise **Pydantic** pour vérifier automatiquement les données.
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item
```

---

## ⚖️ Injection de dépendances
FastAPI permet de passer des objets comme une session DB automatiquement :
```python
@app.get("/items/")
async def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

---

## 🔒 Sécurité (Notions)
- Authentification avec **OAuth2** ou **JWT**
- Gestion des rôles (RBAC)
- Protection contre attaques courantes (SQLi, XSS, CSRF)

---

## 📅 ORM avec SQLAlchemy
Intégration native avec SQLAlchemy pour les bases SQL (PostgreSQL, MySQL, etc).
```python
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

---

## 🌐 Tests avec Pytest
```python
from fastapi.testclient import TestClient
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
```

---

## 🛁 Déploiement (Docker)
Fichier `Dockerfile` :
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

---

## 🔄 Exemple CRUD complet
```python
items = {}

@app.post("/items/")
async def create_item(item: Item):
    items[item.id] = item
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items[item_id]
```

---

## 📘 Projets types
1. Gestionnaire de tâches (CRUD + utilisateurs)
2. Blog (Articles + Commentaires + Auth)
3. Suivi des dépenses (visualisation + API)

---

## 🌐 Stack recommandée pour projet :
- **Frontend** : Streamlit
- **Backend** : FastAPI
- **Base de données** : Supabase
- **Tests** : PyTest
- **Conteneurisation** : Docker
- **CI/CD** : GitHub Actions