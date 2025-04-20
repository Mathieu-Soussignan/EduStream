import streamlit as st
from streamlit_ace import st_ace

from utils.file_operations import save_course_file
from utils.metadata_operations import load_metadata, save_metadata
from utils.supabase_operations import add_course_to_db


def add_course_page() -> None:
    """Page d’ajout / modification d’un cours avec éditeur Markdown live‑preview."""

    st.title("📘 Ajouter un nouveau cours")

    # ────────────────────────────────────────────────────────────────────────────
    # MÉTADONNÉES DU COURS
    # ────────────────────────────────────────────────────────────────────────────
    title: str = st.text_input("Titre du cours")
    category: str = st.text_input("Catégorie")
    contributor: str = st.text_input("Nom ou e‑mail du contributeur")

    st.markdown("### Contenu du cours")

    # ────────────────────────────────────────────────────────────────────────────
    # ÉDITEUR MARKDOWN & LIVE PREVIEW (Ace Editor)
    # ────────────────────────────────────────────────────────────────────────────
    col_editor, col_preview = st.columns([3, 3])

    with col_editor:
        content: str | None = st_ace(
            placeholder="Écris ton markdown ici…",
            language="markdown",
            theme="github",
            key="markdown_editor",
            height=400,
            wrap=True,
            auto_update=True,
        )

    with col_preview:
        st.markdown("#### Aperçu")
        st.markdown(content or "_Commence ta rédaction…_")

    # ────────────────────────────────────────────────────────────────────────────
    # ACTIONS
    # ────────────────────────────────────────────────────────────────────────────
    if st.button("💾 Sauvegarder le cours"):
        # Validation basique
        if not title or not category or not content or not contributor:
            st.warning("Merci de remplir **titre, catégorie, contenu et contributeur**.")
            st.stop()

        # Sauvegarde locale (markdown)
        filename: str = title.lower().replace(" ", "_") + ".md"
        save_course_file(category, filename, content)

        # Sauvegarde métadonnées locales
        metadata: dict = load_metadata()
        metadata[filename] = {
            "title": title,
            "category": category,
            "author": contributor,
        }
        save_metadata(metadata)

        # Push vers Supabase
        supa_result = add_course_to_db(
            titre=title,
            categorie=category,
            contenu=content,
            auteur=contributor,
        )

        if "error" in supa_result:
            st.warning(
                f"⚠️ Cours enregistré localement, mais erreur Supabase : {supa_result['error']}"
            )
        else:
            st.success("✅ Cours sauvegardé et ajouté à Supabase.")