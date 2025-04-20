import streamlit as st
from utils.supabase_operations import get_all_courses, get_course_by_id
from utils import ia_summary_agent  # ✅ Seul import IA maintenant


def view_courses_page():
    st.title("📚 Voir les cours")

    cours = get_all_courses()
    if not cours:
        st.info("Aucun cours disponible.")
        return

    search_term = st.text_input("Rechercher par titre", "").lower()

    categories = sorted(list(set(
        c.get("categorie", "Non classé") for c in cours if isinstance(c, dict)
    )))
    selected_category = st.selectbox("Filtrer par catégorie", ["Toutes"] + categories)

    filtered_courses = [
        c for c in cours
        if isinstance(c, dict)
        and (selected_category == "Toutes" or c.get("categorie") == selected_category)
        and search_term in c.get("titre", "").lower()
    ]

    if not filtered_courses:
        st.warning("Aucun cours trouvé.")
        return

    for course in filtered_courses:
        with st.expander(f"📘 {course['titre']}"):
            st.markdown(f"**🗂️ Catégorie** : `{course.get('categorie', 'Non classé')}`")
            st.markdown(f"**✍️ Contributeur** : `{course.get('auteur', 'Non renseigné')}`")
            st.markdown(f"**📅 Date** : `{course.get('date_creation', 'Inconnue')}`")
            st.markdown("---")
            if st.button("📖 Ouvrir le cours", key=course['id']):
                print("🔗 Accès au détail du cours :", course['titre'])
                st.session_state.selected_course = course['id']
                st.session_state.page = "Voir le cours en détail"

def view_course_detail_page():
    # 🔒 Vérifie que l’ID du cours est bien défini
    print("🚀 Chargement de la page détail du cours")
    if "selected_course" not in st.session_state or st.session_state.selected_course is None:
        st.error("Aucun cours sélectionné.")
        return

    # 🔁 Assure que la page actuelle est bien la bonne
    st.session_state.page = "Voir le cours en détail"

    course_id = st.session_state.selected_course
    course = get_course_by_id(course_id)

    if course:
        st.title(course["titre"])
        st.markdown(f"**🗂️ Catégorie** : `{course.get('categorie', 'Non classé')}`")
        st.markdown(f"**✍️ Contributeur** : `{course.get('auteur', 'Non renseigné')}`")
        st.markdown(f"**📅 Date** : `{course.get('date_creation', 'Inconnue')}`")
        st.markdown("---")
        st.markdown(course["contenu"], unsafe_allow_html=True)

        print(f"🧪 Longueur du contenu : {len(course['contenu'].strip())}")

        # Initialiser le flag pour le résumé
        if "generate_summary" not in st.session_state:
            st.session_state.generate_summary = False

        if len(course["contenu"].strip()) > 80:
            if not st.session_state.generate_summary:
                if st.button("🧠 Générer un résumé automatique"):
                    print("🧠 Bouton de génération cliqué !")
                    st.session_state.generate_summary = True
                    st.rerun()
            else:
                with st.spinner("Chargement du modèle et génération du résumé..."):
                    model = ia_summary_agent.load_summary_model()
                    summary = ia_summary_agent.summarize(course["contenu"], model)
                    print("📝 Résumé généré :", summary)
                    st.markdown("### 📝 Résumé généré par l'IA :")
                    st.success(summary)

                if st.button("↩️ Réinitialiser le résumé"):
                    st.session_state.generate_summary = False
                    st.rerun()
        else:
            st.info("📄 Le contenu est trop court pour être résumé automatiquement.")

        if st.button("✏️ Modifier le cours"):
            st.session_state.page = "Modifier le cours"
            st.session_state.selected_course = course_id
    else:
        st.error("Erreur lors du chargement du cours.")