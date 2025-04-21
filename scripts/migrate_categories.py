from utils.supabase_operations import supabase


def migrate_categories_from_courses():
    res = supabase.table("cours").select("categorie").execute()
    cours = res.data

    categories = {c["categorie"].strip() for c in cours if c.get("categorie")}
    print(f"🔎 Catégories détectées : {categories}")

    for nom in categories:
        try:
            supabase.table("categories").insert({"nom": nom}).execute()
            print(f"✅ Ajouté : {nom}")
        except Exception as e:
            print(f"⚠️ Erreur pour {nom} : {e}")

if __name__ == "__main__":
    migrate_categories_from_courses()