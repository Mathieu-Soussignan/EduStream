import os
from dotenv import load_dotenv
from supabase import create_client
import streamlit as st

# Charger les variables d’environnement
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# 🔐 PAGE DE LOGIN
def login_page():
    st.title("🔐 Connexion à EduStream")
    tab1, tab2 = st.tabs(["Connexion", "Créer un compte"])

    # Connexion
    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_password")

        if st.button("Se connecter"):
            try:
                result = supabase.auth.sign_in_with_password({"email": email, "password": password})
                if result:
                    st.session_state.authenticated = True
                    st.session_state.user = result.user
                    st.session_state.token = result.session.access_token
                    st.success("Connexion réussie ✅")
                    st.rerun()
            except Exception as e:
                st.error("❌ Connexion échouée : " + str(e))

    # Création de compte
    with tab2:
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Mot de passe", type="password", key="signup_password")

        if st.button("Créer un compte"):
            try:
                result = supabase.auth.sign_up({"email": email, "password": password})
                st.success("✅ Compte créé ! Vérifie ton email pour confirmer l'inscription.")
            except Exception as e:
                st.error("❌ Erreur lors de l'inscription : " + str(e))


# 🔓 Déconnexion
def logout():
    for key in ["authenticated", "user", "token"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()


# ✅ Vérification de session
def check_session():
    return st.session_state.get("authenticated", False)