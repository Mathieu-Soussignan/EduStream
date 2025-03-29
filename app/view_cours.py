import streamlit as st
from utils.file_operations import read_course_file
from utils.metadata_operations import load_metadata


def view_courses_page():
    st.title("📚 Voir les cours")

    metadata = load_metadata()
    if not metadata:
        st.info("Aucun cours disponible.")
        return

    # 🔍 Barre de recherche
    search_term = st.text_input("Rechercher par titre", "").lower()

    # 📂 Filtre par catégorie
    categories = sorted(list(set(course["category"] for course in metadata.values())))
    selected_category = st.selectbox("Filtrer par catégorie", ["Toutes"] + categories)

    # 🔎 Filtrage des cours
    filtered_courses = [
        (filename, data) for filename, data in metadata.items()
        if (selected_category == "Toutes" or data["category"] == selected_category)
        and search_term in data["title"].lower()
    ]

    if not filtered_courses:
        st.warning("Aucun cours trouvé.")
        return

    # 🎨 Affichage des cours
    for filename, data in filtered_courses:
        with st.expander(f"📘 {data['title']}"):
            st.markdown(f"**🗂️ Catégorie** : `{data['category']}`")
            st.markdown(f"**✍️ Contributeur** : `{data.get('contributor', 'Non renseigné')}`")
            st.markdown(f"**📅 Date** : `{data.get('date', 'Inconnue')}`")
            st.markdown("---")
            if st.button("📖 Ouvrir le cours", key=filename):
                st.session_state.selected_course = filename
                st.session_state.page = "Voir le cours en détail"


def view_course_detail_page():
    if "selected_course" not in st.session_state:
        st.error("Aucun cours sélectionné.")
        return

    filename = st.session_state.selected_course
    metadata = load_metadata()
    data = metadata.get(filename)

    if data:
        st.title(data["title"])
        st.markdown(f"**🗂️ Catégorie** : `{data['category']}`")
        st.markdown(f"**✍️ Contributeur** : `{data.get('contributor', 'Non renseigné')}`")
        st.markdown(f"**📅 Date** : `{data.get('date', 'Inconnue')}`")
        st.markdown("---")
        content = read_course_file(data["category"], filename)
        st.markdown(content, unsafe_allow_html=True)

        if st.button("✏️ Modifier le cours"):
            st.session_state.page = "Modifier le cours"
            st.session_state.selected_course = filename
    else:
        st.error("Erreur lors du chargement du cours.")