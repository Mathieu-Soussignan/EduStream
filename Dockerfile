# 🔹 1. Image de base légère avec Python
FROM python:3.10-slim

# 🔹 2. Définir le répertoire de travail
WORKDIR /app

# 🔹 3. Copier les fichiers nécessaires
COPY requirements.txt .
COPY . .

# 🔹 4. Installer les dépendances
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 🔹 5. Exposer le port par défaut de Streamlit
EXPOSE 8501

# 🔹 6. Lancer l'application Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false"]