import streamlit as st
from utils.supabase_operations import get_all_courses, get_course_by_id


def view_courses_page():
    st.title("📚 Voir les cours")

    cours = get_all_courses()
    if not cours:
        st.info("Aucun cours disponible.")
        return

    # 🔍 Barre de recherche
    search_term = st.text_input("Rechercher par titre", "").lower()

    # 📂 Filtre par catégorie
    categories = sorted(list(set(c["categorie"] for c in cours)))
    selected_category = st.selectbox("Filtrer par catégorie", ["Toutes"] + categories) # noqa

    # 🔎 Filtrage des cours
    filtered_courses = [
        c for c in cours
        if (selected_category == "Toutes" or c["categorie"] == selected_category) # noqa
        and search_term in c["titre"].lower()
    ]

    if not filtered_courses:
        st.warning("Aucun cours trouvé.")
        return

    # 🎨 Affichage des cours
    for course in filtered_courses:
        with st.expander(f"📘 {course['titre']}"):
            st.markdown(f"**🗂️ Catégorie** : `{course['categorie']}`")
            st.markdown(f"**✍️ Contributeur** : `{course.get('auteur', 'Non renseigné')}`") # noqa
            st.markdown(f"**📅 Date** : `{course.get('date_creation', 'Inconnue')}`") # noqa
            st.markdown("---")
            if st.button("📖 Ouvrir le cours", key=course['id']):
                st.session_state.selected_course = course['id']
                st.session_state.page = "Voir le cours en détail"


def view_course_detail_page():
    if "selected_course" not in st.session_state:
        st.error("Aucun cours sélectionné.")
        return

    course_id = st.session_state.selected_course
    course = get_course_by_id(course_id)

    if course:
        st.title(course["titre"])
        st.markdown(f"**🗂️ Catégorie** : `{course['categorie']}`")
        st.markdown(f"**✍️ Contributeur** : `{course.get('auteur', 'Non renseigné')}`") # noqa
        st.markdown(f"**📅 Date** : `{course.get('date_creation', 'Inconnue')}`") # noqa
        st.markdown("---")
        st.markdown(course["contenu"], unsafe_allow_html=True)

        if st.button("✏️ Modifier le cours"):
            st.session_state.page = "Modifier le cours"
            st.session_state.selected_course = course_id
    else:
        st.error("Erreur lors du chargement du cours.") # noqa