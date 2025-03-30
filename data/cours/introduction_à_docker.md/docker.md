## Qu'est-ce que Docker ?
Docker est une plateforme qui permet de créer, déployer et exécuter des applications dans des conteneurs. Un **conteneur Docker** est un environnement isolé, léger et reproductible qui contient tout le nécessaire pour exécuter une application.

---

## Pourquoi utiliser Docker ?
- Exécuter plusieurs applications isolées sur un même serveur.
- Assurer la **reproductibilité** des environnements.
- Partager facilement des applications via **Docker Hub**.
- Déployer une application sur n'importe quelle machine (Linux, Windows, Cloud, etc).

---

## Dockerfile : Le fichier de construction d'une image Docker

Voici les instructions principales utilisées dans un `Dockerfile` :

- `FROM` : image de base (ex: `python:3.11-slim-buster`)
- `RUN` : exécute une commande (ex: installation de dépendances)
- `WORKDIR` : définit le dossier de travail dans le conteneur
- `COPY` : copie les fichiers locaux vers le conteneur
- `EXPOSE` : spécifie le port à ouvrir
- `CMD` : commande à exécuter au lancement du conteneur

### Exemple complet
```Dockerfile
FROM python:3.11-slim-buster
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "/app/app.py"]
```

---

## Commandes Docker de base

```bash
# Construction de l'image
$ docker build -t monimage:1.0 .

# Exécution d'un conteneur
$ docker run -d -p 8000:5000 --rm monimage:1.0

# Lister les images disponibles
$ docker images

# Lister les conteneurs actifs
$ docker container ls

# Stopper un conteneur
$ docker stop <CONTAINER_ID>

# Supprimer une image
$ docker rmi <IMAGE_ID>

# Se connecter à Docker Hub
$ docker login

# Pousser une image vers Docker Hub
$ docker push <pseudo>/<nom>:<tag>
```

---

## Déploiement avec FastAPI dans un conteneur

### Code Python (app/main.py)
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
```

### Dockerfile pour FastAPI
```Dockerfile
FROM python:3.11-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Lancer l'application FastAPI
```bash
docker run -p 8000:8000 my-fastapi-app
```

---

## CI/CD avec GitHub Actions

### Fichier `.github/workflows/cicd.yml`
```yaml
name: CI/CD
on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Build Docker image
        run: docker build -t votre-organisation/votre-projet .
      - name: Run tests
        run: docker run votre-organisation/votre-projet pytest
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - name: Push Docker image
        run: docker push votre-organisation/votre-projet
```

> Remarque : Pensez à configurer les **secrets GitHub** dans votre dépôt.

---

## Déploiement sur Azure Container Instance (ACI)
1. Créer une instance ACI sur le portail Azure.
2. Définir l'image à partir de Docker Hub : `<pseudo>/<image>:<tag>`
3. Configurer les ressources et le port (ex: 8000).
4. Valider : votre conteneur est en ligne !

---

## Ressources utiles
- [https://hub.docker.com/](https://hub.docker.com/)
- [https://docs.docker.com/](https://docs.docker.com/)
- [Best practices Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)