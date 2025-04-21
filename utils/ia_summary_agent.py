import textwrap

def load_summary_model():
    """
    Modèle français T5 fine-tuné pour le résumé (CNN/DM FR).
    Meilleure stabilité et pertinence sur des contenus pédagogiques.
    """
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

    model_name = "plguillou/t5-base-fr-sum-cnndm"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return pipeline("summarization", model=model, tokenizer=tokenizer)


def split_text(text, max_chunk_length=1000):
    """
    Découpe un long texte en morceaux plus petits, basés sur les sauts de ligne ou les mots.

    Args:
        text (str): Le texte à découper.
        max_chunk_length (int): Longueur max (en caractères) de chaque chunk.

    Returns:
        list[str]: Liste de morceaux de texte.
    """
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 1 <= max_chunk_length:
            current_chunk += paragraph + "\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def summarize(text, model, max_length=120, min_length=30, max_chunk_length=1000):
    """
    Génère un résumé à partir du texte donné, même s'il est long (en le découpant si nécessaire).

    Args:
        text (str): Le texte à résumer.
        model (pipeline): Le pipeline de summarization préchargé.
        max_length (int): Longueur maximale du résumé.
        min_length (int): Longueur minimale du résumé.
        max_chunk_length (int): Longueur max des morceaux en cas de découpage.

    Returns:
        str: Le résumé généré.
    """
    cleaned_text = text.strip()
    print(f"🧪 Longueur du texte : {len(cleaned_text)} caractères")

    if not cleaned_text or len(cleaned_text) < 50:
        print("❌ Texte trop court pour le résumé.")
        return "⛔ Le texte est trop court pour être résumé."

    print("🧩 Vérification de la longueur...")
    if len(cleaned_text) > max_chunk_length:
        print("✂️ Texte trop long : découpage en morceaux...")
        chunks = split_text(cleaned_text, max_chunk_length=max_chunk_length)
        print(f"📦 {len(chunks)} morceaux à résumer")
        summaries = []
        for i, chunk in enumerate(chunks, 1):
            print(f"🔹 Résumé du morceau {i}/{len(chunks)}...")
            summary = model(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        print("✅ Tous les résumés partiels générés.")
        return "\n\n".join(summaries)
    else:
        print("⚙️ Appel du pipeline de summarization...")
        result = model(cleaned_text, max_length=max_length, min_length=min_length, do_sample=False)
        print("✅ Résumé généré !")
        return result[0]['summary_text']