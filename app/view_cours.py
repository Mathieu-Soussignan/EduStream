import streamlit as st
from utils.file_operations import list_courses, read_course_file
from utils.metadata_operations import load_metadata

def view_courses_page():
    st.title("Voir les cours")

    metadata = load_metadata()
    categories = list(set(course["category"] for course in metadata.values()))

    selected_category = st.selectbox("Sélectionner une catégorie", ["Toutes"] + categories)

    # Filtrer les cours par catégorie
    filtered_courses = [
        (filename, data) for filename, data in metadata.items()
        if selected_category == "Toutes" or data["category"] == selected_category
    ]

    if not filtered_courses:
        st.info("Aucun cours disponible.")
        return

    for filename, data in filtered_courses:
        if st.button(data["title"]):
            content = read_course_file(data["category"], filename)
            st.markdown(content, unsafe_allow_html=True)

def view_course_detail_page():
    if "selected_course" not in st.session_state:
        st.error("Aucun cours sélectionné.")
        return

    filename = st.session_state.selected_course
    metadata = load_metadata()
    data = metadata.get(filename)

    if data:
        st.title(data["title"])
        content = read_course_file(data["category"], filename)
        st.markdown(content, unsafe_allow_html=True)
        if st.button("Modifier le cours"):
            st.session_state.page = "Modifier le cours"
            st.session_state.selected_course = filename
    else:
        st.error("Erreur lors du chargement du cours.")