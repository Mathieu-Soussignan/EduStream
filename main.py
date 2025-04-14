# ✅ La config DOIT être la première commande Streamlit
import os
os.environ["PYTORCH_JIT"] = "0"

import streamlit as st
from app.add_cours import add_course_page
from app.view_cours import view_courses_page, view_course_detail_page
from app.manage_categories import manage_categories_page
from app.auth_supabase import login_page, logout, check_session

# ✅ Configuration de la page
st.set_page_config(page_title="EduStream IA", layout="wide")

# 🔐 Authentification Supabase
if not check_session():
    login_page()
    st.stop()

# ✅ Header utilisateur connecté
user = st.session_state.get("user")
st.sidebar.markdown(f"👤 Connecté : `{user.email}`")

# 🚪 Déconnexion
if st.sidebar.button("🚪 Se déconnecter"):
    logout()

# 📌 Menu de navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Aller à",
    [
        "🏠 Accueil",
        "📘 Ajouter un cours",
        "📚 Voir les cours",
        "🗂️ Gérer les catégories",
    ]
)

# 🧼 Nettoyage des états dynamiques
st.session_state.pop("page", None)
st.session_state.pop("selected_course", None)

# === Pages principales ===
if page == "🏠 Accueil":
    st.title("🎓 Bienvenue sur EduStream")
    st.subheader("La plateforme de cours IA collaborative de l’école Microsoft by Simplon")

    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown("""
        👋 Cette application te permet :
        - 📘 d’**ajouter** tes cours
        - 📚 de **consulter** ceux de ta promo
        - 🛠️ de **modifier** les contenus
        - 🗂️ de **gérer les catégories**

        > 🤝 Objectif : centraliser notre apprentissage et progresser ensemble.
        """)
    with col2:
        st.image("./assets/home_ai.jpg", use_container_width=True)

    st.divider()
    st.info("💡 N’oublie pas de renseigner ton nom/email quand tu ajoutes un cours !")

elif page == "📘 Ajouter un cours":
    add_course_page()

elif page == "📚 Voir les cours":
    view_courses_page()

elif page == "🗂️ Gérer les catégories":
    manage_categories_page()

# === Pages dynamiques internes ===
if "page" in st.session_state:
    if st.session_state.page == "Voir le cours en détail":
        view_course_detail_page()
    elif st.session_state.page == "Modifier le cours":
        add_course_page()