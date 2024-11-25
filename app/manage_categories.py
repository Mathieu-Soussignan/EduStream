
import streamlit as st
import os
from utils.metadata_operations import load_metadata, save_metadata

DATA_PATH = "data/cours"

def manage_categories_page():
    st.title("Gérer les catégories")

    # Charger les métadonnées existantes
    metadata = load_metadata()
    existing_categories = list(set(data["category"] for data in metadata.values()))

    # Afficher les catégories existantes
    st.subheader("Catégories existantes")
    if existing_categories:
        for category in existing_categories:
            st.text(category)
    else:
        st.info("Aucune catégorie trouvée.")

    # Ajouter une nouvelle catégorie
    st.subheader("Ajouter une catégorie")
    new_category = st.text_input("Nom de la nouvelle catégorie")

    if st.button("Ajouter une catégorie"):
        if new_category and new_category not in existing_categories:
            category_path = os.path.join(DATA_PATH, new_category)
            os.makedirs(category_path, exist_ok=True)
            st.success(f"La catégorie '{new_category}' a été ajoutée.")
        else:
            st.error("Cette catégorie existe déjà ou le champ est vide.")

    # Supprimer une catégorie existante
    st.subheader("Supprimer une catégorie")
    category_to_delete = st.selectbox("Choisir une catégorie à supprimer", existing_categories)

    if st.button("Supprimer la catégorie"):
        if category_to_delete:
            # Supprimer le dossier et ses fichiers
            category_path = os.path.join(DATA_PATH, category_to_delete)
            if os.path.exists(category_path):
                for file in os.listdir(category_path):
                    os.remove(os.path.join(category_path, file))
                os.rmdir(category_path)

            # Mettre à jour les métadonnées
            metadata = {
                k: v for k, v in metadata.items() if v["category"] != category_to_delete
            }
            save_metadata(metadata)

            st.success(f"La catégorie '{category_to_delete}' a été supprimée.")
        else:
            st.error("Aucune catégorie sélectionnée.")