import streamlit as st
from utils.file_operations import save_course_file, list_courses, read_course_file
from utils.metadata_operations import load_metadata, save_metadata


def add_course_page():
    st.title("Ajouter un cours")

    # Si on est en mode modification, pré-remplir les champs
    if "selected_course" in st.session_state and st.session_state.page == "Modifier le cours":
        filename = st.session_state.selected_course
        metadata = load_metadata()
        course_data = metadata.get(filename, {})

        title = st.text_input("Titre du cours", value=course_data.get("title", ""))
        category = st.text_input("Catégorie", value=course_data.get("category", ""))
        content = st.text_area("Contenu du cours (en Markdown)", value=read_course_file(course_data.get("category", ""), filename))
        contributor = st.text_input("Nom ou Email du contributeur", value=course_data.get("contributor", ""))
        is_edit = True
    else:
        title = st.text_input("Titre du cours")
        category = st.text_input("Catégorie")
        content = st.text_area("Contenu du cours (en Markdown)")
        contributor = st.text_input("Nom ou Email du contributeur")
        is_edit = False

    # Afficher les catégories existantes
    metadata = load_metadata()
    existing_categories = list(set(course["category"] for course in metadata.values()))
    if existing_categories:
        st.write("Catégories existantes :", ", ".join(existing_categories))

    # Validation des champs
    if st.button("Aperçu du cours"):
        if not title or not category or not content or not contributor:
            st.error("Veuillez remplir tous les champs.")
        elif title in [course["title"] for course in metadata.values()] and not is_edit:
            st.error("Un cours avec ce titre existe déjà. Veuillez en choisir un autre.")
        else:
            st.markdown("## Aperçu du cours")
            st.markdown(f"### {title}")
            st.markdown(content, unsafe_allow_html=True)
            st.markdown(f"**Contributeur :** {contributor}")

    if st.button("Sauvegarder le cours"):
        if not title or not category or not content or not contributor:
            st.error("Veuillez remplir tous les champs.")
        elif title in [course["title"] for course in metadata.values()] and not is_edit:
            st.error("Un cours avec ce titre existe déjà. Veuillez en choisir un autre.")
        else:
            # Sauvegarder le cours
            filename = f"{title.replace(' ', '_').lower()}.md"
            save_course_file(category, filename, content)

            # Mettre à jour les métadonnées
            metadata[filename] = {"title": title, "category": category, "contributor": contributor}
            save_metadata(metadata)

            st.success("Cours sauvegardé avec succès!")
            # Réinitialiser l'état si on modifie un cours
            if is_edit:
                del st.session_state.selected_course
                st.session_state.page = "Voir les cours"