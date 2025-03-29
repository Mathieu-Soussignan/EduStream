import streamlit as st
from datetime import datetime
from utils.file_operations import save_course_file, list_courses, read_course_file
from utils.metadata_operations import load_metadata, save_metadata

def add_course_page():
    st.title("📘 Ajouter ou Modifier un cours")

    metadata = load_metadata()

    # Mode édition : on pré-remplit les champs
    is_edit = "selected_course" in st.session_state and st.session_state.page == "Modifier le cours"

    if is_edit:
        filename = st.session_state.selected_course
        course_data = metadata.get(filename, {})
        title = st.text_input("Titre du cours", value=course_data.get("title", ""))
        category = st.text_input("Catégorie", value=course_data.get("category", ""))
        content = st.text_area("Contenu du cours (Markdown)", value=read_course_file(course_data.get("category", ""), filename))
        contributor = st.text_input("Nom ou Email du contributeur", value=course_data.get("contributor", ""))
    else:
        title = st.text_input("Titre du cours")
        category = st.text_input("Catégorie")
        content = st.text_area("Contenu du cours (Markdown)")
        contributor = st.text_input("Nom ou Email du contributeur")

    # 🗂️ Catégories existantes
    existing_categories = list(set(course["category"] for course in metadata.values()))
    if existing_categories:
        st.markdown("**Catégories déjà créées :**")
        st.code(", ".join(sorted(existing_categories)))

    # 📄 Aperçu du cours
    if st.button("📄 Aperçu du cours"):
        if not title or not category or not content or not contributor:
            st.error("Tous les champs doivent être remplis.")
        elif title in [course["title"] for course in metadata.values()] and not is_edit:
            st.error("Un cours avec ce titre existe déjà.")
        else:
            st.markdown("---")
            st.subheader(title)
            st.markdown(f"**Catégorie :** `{category}`")
            st.markdown(f"**Contributeur :** `{contributor}`")
            st.markdown(content, unsafe_allow_html=True)

    # 💾 Sauvegarde
    if st.button("💾 Sauvegarder le cours"):
        if not title or not category or not content or not contributor:
            st.error("Tous les champs doivent être remplis.")
        elif title in [course["title"] for course in metadata.values()] and not is_edit:
            st.error("Un cours avec ce titre existe déjà.")
        else:
            filename = f"{title.replace(' ', '_').lower()}.md"
            save_course_file(category, filename, content)

            metadata[filename] = {
                "title": title,
                "category": category,
                "contributor": contributor,
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            save_metadata(metadata)

            st.success("✅ Cours sauvegardé avec succès !")

            if is_edit:
                del st.session_state.selected_course
                st.session_state.page = "Voir les cours"