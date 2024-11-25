import streamlit as st
from app.add_cours import add_course_page
from app.view_cours import view_courses_page, view_course_detail_page
from app.manage_categories import manage_categories_page

# Sidebar navigation
st.sidebar.title("Navigation")

# Ajout de l'option dans la navigation
page = st.sidebar.radio(
    "Aller à",
    [
        "🏠 Accueil",
        "📘 Ajouter un cours",
        "📚 Voir les cours",
        "🗂️ Gérer les catégories",
    ]
)

# Gestion de la navigation à partir de la barre latérale
if page == "🏠 Accueil":
    st.title("Bienvenue sur EduStream - la Plateforme de Cours IA collaborative de l'école Microsoft by Simplon 🎓")
    st.write("""
    Cette application est conçue pour vous permettre de gérer vos cours de manière simple et intuitive.
    Utilisez le menu de navigation sur la gauche pour accéder aux différentes fonctionnalités.
    """)
    st.image("./assets/home_ai.jpg", caption="Apprentissage interactif avec vos cours d'IA")

elif page == "📘 Ajouter un cours":
    add_course_page()

elif page == "📚 Voir les cours":
    view_courses_page()

elif page == "🗂️ Gérer les catégories":
    manage_categories_page()

# Gestion des pages dynamiques définies par `session_state`
if "page" in st.session_state:
    if st.session_state.page == "Voir le cours en détail":
        view_course_detail_page()
    elif st.session_state.page == "Modifier le cours":
        add_course_page()  # Utilisation de `add_course_page` pour la modification