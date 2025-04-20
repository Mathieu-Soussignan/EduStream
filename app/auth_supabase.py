import os
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
SITE_URL = os.getenv("SITE_URL", "http://localhost:8501")

supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


# ── AUTHENTIFICATION UTILISATEUR ────────────────────────────────────────────
def authenticate_user(email: str, password: str) -> dict | None:
    try:
        result = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })

        if not result.user.email_confirmed_at:
            return None

        user = result.user
        token = result.session.access_token

        # Chargement du profil utilisateur
        resp = (
            supabase.table("profiles")
            .select("role, display_name, avatar_url")
            .eq("id", user.id)
            .execute()
        )
        rows = resp.data or []

        if rows:
            profile = rows[0]
        else:
            # Création du profil si inexistant
            profile = {
                "id": user.id,
                "role": "user",
                "display_name": "",
                "avatar_url": "",
            }
            supabase.table("profiles").insert(profile).execute()

        return {
            "user": user,
            "token": token,
            "profile": profile,
        }

    except Exception as e:
        print("❌ Erreur d'authentification :", e)
        return None


# ── CRÉATION DE COMPTE ───────────────────────────────────────────────────────
def create_user(email: str, password: str) -> tuple[bool, str]:
    try:
        result = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "email_redirect_to": f"{SITE_URL}/?confirm",
            },
        })
        return True, result
    except Exception as e:
        return False, str(e)


# ── LOGOUT ──────────────────────────────────────────────────────────────────
def logout() -> None:
    for key in [
        "authenticated", "user", "token",
        "user_role", "avatar_url", "display_name"
    ]:
        st.session_state.pop(key, None)
    st.rerun()


# ── CHECK SESSION ───────────────────────────────────────────────────────────
def check_session() -> bool:
    return st.session_state.get("authenticated", False)