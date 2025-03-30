import os
from dotenv import load_dotenv
from supabase import create_client

# Charger les variables .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialiser Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# Requête simple : récupérer tous les cours
def test_fetch_courses():
    try:
        response = supabase.table("cours").select("*").execute()
        print("✅ Connexion réussie !")
        print(f"{len(response.data)} cours trouvés.")
        for cours in response.data:
            print(f"- {cours['titre']} (par {cours['auteur']})")
    except Exception as e:
        print("❌ Erreur de connexion à Supabase :")
        print(e)

# Lancer le test
if __name__ == "__main__":
    test_fetch_courses()