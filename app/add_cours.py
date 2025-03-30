import streamlit as st
import os # noqa
from utils.file_operations import save_course_file
from utils.metadata_operations import save_metadata, load_metadata
from utils.supabase_operations import add_course_to_db


def add_course_page():
    st.title("Ajouter un nouveau cours")

    title = st.text_input("Titre du cours")
    category = st.text_input("Catégorie")
    contributor = st.text_input("Nom ou email du contributeur")
    content = st.text_area("Contenu du cours (Markdown)", height=300)

    if st.button("💾 Sauvegarder le cours"):
        if not title or not category or not content or not contributor:
            st.warning("Merci de remplir tous les champs.")
            return

        filename = title.lower().replace(" ", "_") + ".md"
        save_course_file(category, filename, content)

        metadata = load_metadata()
        metadata[filename] = {
            "title": title,
            "category": category,
            "author": contributor
        }
        save_metadata(metadata)

        st.success("Cours sauvegardé avec succès !")

        # Envoi vers Supabase
        supabase_response = add_course_to_db(
            titre=title,
            categorie=category,
            contenu=content,
            auteur=contributor
        )

        if "error" in supabase_response:
            st.warning(f"⚠️ Cours enregistré localement, mais erreur Supabase : {supabase_response['error']}") # noqa
        else:
            st.info("✅ Le cours a également été ajouté à la base collaborative Supabase.")  # noqa