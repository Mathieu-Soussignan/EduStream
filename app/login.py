import streamlit as st
from auth_supabase import create_user, authenticate_user


def login_page():
    st.title("🔐 Connexion à EduStream")

    tab1, tab2 = st.tabs(["Se connecter", "Créer un compte"])

    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_pass")
        if st.button("Connexion"):
            result = authenticate_user(email, password)
            if result:
                st.session_state.authenticated = True
                st.session_state.user = result["user"]
                st.session_state.token = result["token"]
                st.success("Connexion réussie ✅")
                st.rerun()
            else:
                st.error("❌ Identifiants incorrects")

    with tab2:
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Mot de passe", type="password", key="signup_pass")
        if st.button("Créer un compte"):
            success, result = create_user(email, password)
            if success:
                st.success("Compte créé ! Vérifie tes mails 📩")
            else:
                st.error(f"Erreur : {result}")