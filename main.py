import os
os.environ["PYTORCH_JIT"] = "0"

import streamlit as st

from app.add_cours import add_course_page
from app.view_cours import view_courses_page, view_course_detail_page
from app.manage_categories import manage_categories_page
from app.login import login_page
from app.auth_supabase import logout, check_session
from app.profile_page import profile_page

# ────────────────────────────────────────────────────────────────────────────────
# CONFIG STREAMLIT
# ────────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="EduStream IA", layout="wide")

# ────────────────────────────────────────────────────────────────────────────────
# AUTH
# ────────────────────────────────────────────────────────────────────────────────
if not check_session():
    # Cas particulier : l’utilisateur vient de s’inscrire mais n’a pas confirmé
    if st.session_state.get("pending_confirmation"):
        st.info(
            "📧 Un e‑mail de confirmation t’a été envoyé. "
            "Clique sur le lien puis connecte‑toi."
        )

    # On affiche la page login/signup
    login_page()
    st.stop()

# ────────────────────────────────────────────────────────────────────────────────
# UTILISATEUR CONNECTÉ
# ────────────────────────────────────────────────────────────────────────────────
user = st.session_state.get("user")
user_role = st.session_state.get("user_role", "user")

# Avatar ou placeholder
avatar_url = st.session_state.get("avatar_url", "")
avatar_display = avatar_url or "https://placehold.co/64x64?text=👤"

print("🖼️ Avatar affiché :", st.session_state.get("avatar_url"))

with st.sidebar:
    st.image(avatar_display, width=64)
    st.markdown(f"**{user.email}**")
    st.markdown(f"🔑 rôle : **{user_role}**")

    if st.button("🚪 Se déconnecter"):
        logout()

# ────────────────────────────────────────────────────────────────────────────────
# NAVIGATION
# ────────────────────────────────────────────────────────────────────────────────
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Aller à",
    [
        "🏠 Accueil",
        "📘 Ajouter un cours",
        "📚 Voir les cours",
        "🗂️ Gérer les catégories",
        "👤 Profil collaborateur",
    ],
)

# Réinitialisation d’éventuels états internes
st.session_state.pop("page", None)
st.session_state.pop("selected_course", None)

# ────────────────────────────────────────────────────────────────────────────────
# PAGES PRINCIPALES
# ────────────────────────────────────────────────────────────────────────────────
if page == "🏠 Accueil":
    st.title("🎓 Bienvenue sur EduStream")
    st.subheader("La plateforme de cours IA collaborative de l’école Microsoft by Simplon")

    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown(
            """
            👋 Cette application te permet :
            - 📘 d’**ajouter** tes cours
            - 📚 de **consulter** ceux de ta promo
            - 🛠️ de **modifier** les contenus
            - 🗂️ de **gérer les catégories**

            > 🤝 Objectif : centraliser notre apprentissage et progresser ensemble.
            """
        )
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
elif page == "👤 Profil collaborateur":
    profile_page()

# ────────────────────────────────────────────────────────────────────────────────
# PAGES DYNAMIQUES INTERNES
# ────────────────────────────────────────────────────────────────────────────────
if "page" in st.session_state:
    if st.session_state.page == "Voir le cours en détail":
        view_course_detail_page()
    elif st.session_state.page == "Modifier le cours":
        add_course_page()