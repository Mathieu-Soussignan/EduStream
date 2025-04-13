import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

# === Chargement des variables d’environnement ===
load_dotenv()
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# === Vérification des variables ===
if not all([GMAIL_ADDRESS, APP_PASSWORD, TO_EMAIL]):
    raise ValueError("❌ Certaines variables d’environnement sont manquantes.")

# === Création du message ===
subject = "📌 Rappel Supabase - Garde ta base active !"
body = f"""
Salut Mathieu,

Petit rappel automatique pour que tu penses à te connecter à ton projet Supabase au moins une fois tous les 90 jours.

🗓 Nous sommes le {datetime.now().strftime('%d/%m/%Y')}

Tu peux te connecter ici 👉 https://app.supabase.com/project/vqymyuetwywrruqeqtib

📌 Ce message est généré automatiquement par ton appli EduStream.

Bonne journée 🚀
"""

msg = EmailMessage()
msg["From"] = GMAIL_ADDRESS
msg["To"] = TO_EMAIL
msg["Subject"] = subject
msg.set_content(body)

# === Envoi du mail ===
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(GMAIL_ADDRESS, APP_PASSWORD)
        server.send_message(msg)
    print("✅ Email de rappel envoyé avec succès !")
except Exception as e:
    print(f"❌ Erreur lors de l'envoi du mail : {e}")