def load_summary_model():
    """
    Charge dynamiquement le pipeline de summarization sans être importé au démarrage,
    pour éviter les conflits avec le watcher Streamlit.
    """
    print("🚀 Chargement du modèle Hugging Face...")
    from transformers import pipeline
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def summarize(text, model, max_length=120, min_length=30):
    """
    Génère un résumé à partir du texte donné.

    Args:
        text (str): Texte à résumer.
        model (pipeline): pipeline de summarization préchargé.
        max_length (int): longueur max du résumé.
        min_length (int): longueur min du résumé.

    Returns:
        str: Le résumé généré.
    """
    print(f"🧪 Longueur du texte : {len(text.strip())}")

    if not text or len(text.strip()) < 50:
        print("❌ Texte trop court pour le résumé.")
        return "⛔ Le texte est trop court pour être résumé."

    print("⚙️ Appel du pipeline de summarization...")
    result = model(text, max_length=max_length, min_length=min_length, do_sample=False)
    print("✅ Résumé généré !")
    return result[0]['summary_text']