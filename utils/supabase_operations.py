from supabase import create_client, Client
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# --- COURS ---
def add_course_to_db(titre, categorie, contenu, auteur):
    date_creation = datetime.now().isoformat()
    data = {
        "titre": titre,
        "categorie": categorie,
        "contenu": contenu,
        "auteur": auteur,
        "date_creation": date_creation
    }
    try:
        response = supabase.table("cours").insert(data).execute()
        return response
    except Exception as e:
        return {"error": str(e)}


def get_all_courses():
    try:
        response = supabase.table("cours").select("*").execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}


def get_courses_by_category(categorie):
    try:
        response = supabase.table("cours").select("*").eq("categorie", categorie).execute() # noqa
        return response.data
    except Exception as e:
        return {"error": str(e)}


def get_course_by_id(course_id):
    try:
        response = supabase.table("cours").select("*").eq("id", course_id).single().execute() # noqa
        return response.data
    except Exception as e:
        return {"error": str(e)}


def update_course(course_id, new_data):
    try:
        response = supabase.table("cours").update(new_data).eq("id", course_id).execute() # noqa
        return response
    except Exception as e:
        return {"error": str(e)}


# --- CATÉGORIES ---
def get_all_categories():
    try:
        response = supabase.table("categories").select("*").execute()
        return response.data
    except Exception as e:  # noqa
        return []


def add_category_to_db(nom):
    try:
        response = supabase.table("categories").insert({"nom": nom}).execute()
        return response
    except Exception as e:
        return {"error": str(e)}


def delete_category_from_db(category_id):
    try:
        response = supabase.table("categories").delete().eq("id", category_id).execute() # noqa
        return response
    except Exception as e:
        return {"error": str(e)}