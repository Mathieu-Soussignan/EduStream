# ✅ La config DOIT être la première commande Streamlit
import streamlit as st
st.set_page_config(page_title="EduStream IA", layout="wide")

from app.add_cours import add_course_page
from app.view_cours import view_courses_page, view_course_detail_page
from app.manage_categories import manage_categories_page

# 📌 Barre latérale de navigation
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

# Réinitialiser certains états
st.session_state.pop("page", None)
st.session_state.pop("selected_course", None)

# 🏠 Page d'accueil
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

# 📘 Ajout de cours
elif page == "📘 Ajouter un cours":
    add_course_page()

# 📚 Consultation des cours
elif page == "📚 Voir les cours":
    view_courses_page()

# 🗂️ Gestion des catégories
elif page == "🗂️ Gérer les catégories":
    manage_categories_page()

# ⚙️ Pages dynamiques (via bouton interne)
if "page" in st.session_state:
    if st.session_state.page == "Voir le cours en détail":
        view_course_detail_page()
    elif st.session_state.page == "Modifier le cours":
        add_course_page()