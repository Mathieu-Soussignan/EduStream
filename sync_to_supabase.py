import os
import json
from dotenv import load_dotenv
from utils.file_operations import read_course_file
from utils.supabase_operations import add_course_to_db
from utils.metadata_operations import load_metadata

load_dotenv()

def sync_courses():
    metadata = load_metadata()
    success = 0

    for filename, data in metadata.items():
        try:
            content = read_course_file(data["category"], filename)
            titre = data["title"]
            categorie = data["category"]
            auteur = data.get("author", "Inconnu")

            response = add_course_to_db(titre, categorie, content, auteur)
            if "error" in response:
                print(f"❌ Échec : {titre} > {response['error']}")
            else:
                print(f"✅ Ajouté : {titre}")
                success += 1
        except Exception as e:
            print(f"⚠️ Erreur pour {filename} : {e}")

    print(f"\n🎯 {success} cours ajoutés avec succès.")

if __name__ == "__main__":
    sync_courses()