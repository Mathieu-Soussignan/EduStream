FROM python:3.11-slim

# Installer les dépendances système minimales
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app

# Installer les dépendances Python
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python -c "from transformers import pipeline; pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')"

# Exposer le port de Streamlit
EXPOSE 8501

# Commande de démarrage
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]