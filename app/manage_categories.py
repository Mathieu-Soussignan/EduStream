import streamlit as st
from utils.supabase_operations import get_all_categories, add_category_to_db, delete_category_from_db # noqa


def manage_categories_page():
    st.title("🗂️ Gérer les catégories")

    # Afficher les catégories depuis Supabase
    categories = get_all_categories()

    st.subheader("Catégories existantes")
    if not categories:
        st.info("Aucune catégorie enregistrée.")
    else:
        for cat in categories:
            col1, col2 = st.columns([0.8, 0.2])
            col1.markdown(f"- `{cat['nom']}`")
            if col2.button("❌ Supprimer", key=f"delete_{cat['id']}"):
                delete_category_from_db(cat['id'])
                st.experimental_rerun()

    st.subheader("Ajouter une nouvelle catégorie")
    new_category = st.text_input("Nom de la nouvelle catégorie")

    if st.button("➕ Ajouter la catégorie"):
        if not new_category:
            st.warning("Merci de renseigner un nom de catégorie.")
        else:
            add_category_to_db(new_category)
            st.success("Catégorie ajoutée avec succès !")
            st.experimental_rerun() # noqa