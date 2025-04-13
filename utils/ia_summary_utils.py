import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_summarizer():
    print("⏳ Chargement du modèle IA résumé...")
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def generate_summary(text, summarizer, max_length=120, min_length=30):
    """
    Génère un résumé à partir d'un texte Markdown ou brut.

    Args:
        text (str): Le contenu du cours à résumer.
        summarizer: le pipeline Hugging Face préchargé
        max_length (int): Longueur maximale du résumé.
        min_length (int): Longueur minimale du résumé.

    Returns:
        str: Résumé généré par le modèle.
    """
    if not text or len(text.strip()) < 50:
        return "Le texte est trop court pour être résumé."

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


# Interface de démo Streamlit pour test local
if __name__ == "__main__":
    st.title("🔄 Générateur de résumé automatique (IA)")

    user_input = st.text_area("📄 Colle ton texte de cours ici :", height=300)

    if st.button("🌐 Générer le résumé"):
        with st.spinner("Analyse en cours..."):
            summarizer = load_summarizer()
            result = generate_summary(user_input, summarizer)
            st.subheader("🔹 Résumé généré :")
            st.success(result)