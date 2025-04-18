import os
from dotenv import load_dotenv
import streamlit as st
from supabase import create_client

# ── ENV & CLIENT ───────────────────────────────────────────────────────────
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SITE_URL     = os.getenv("SITE_URL", "http://localhost:8501")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ── PAGE LOGIN / SIGNUP ────────────────────────────────────────────────────
def login_page() -> None:
    st.title("🔐 Connexion à EduStream")
    tab_login, tab_signup = st.tabs(["Connexion", "Créer un compte"])

    # ── Connexion ──────────────────────────────────────────────────────────
    with tab_login:
        email    = st.text_input("Email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_pwd")

        if st.button("Se connecter"):
            try:
                result = supabase.auth.sign_in_with_password(
                    {"email": email, "password": password}
                )

                # 1️⃣  Vérif e‑mail confirmé
                if not result.user.email_confirmed_at:
                    st.warning("📧 Confirme d’abord ton e‑mail.")
                    return

                # 2️⃣  Stock session auth
                st.session_state.authenticated = True
                st.session_state.user          = result.user
                st.session_state.token         = result.session.access_token

                # 3️⃣  Rôle & profil (robuste)
                resp = (
                    supabase.table("profiles")
                    .select("role, display_name, avatar_url")
                    .eq("id", result.user.id)
                    .execute()
                )
                rows = resp.data or []

                if rows:
                    profile = rows[0]
                else:       # crée la ligne si absente
                    profile = {
                        "id":   result.user.id,
                        "role": "user",
                        "display_name": "",
                        "avatar_url": "",
                    }
                    supabase.table("profiles").insert(profile).execute()

                st.session_state.user_role     = profile["role"]
                st.session_state.display_name  = profile.get("display_name", "")
                st.session_state.avatar_url    = profile.get("avatar_url", "")

                st.success("Connexion réussie ✅")
                st.rerun()

            except Exception as e:
                st.error(f"❌ Connexion échouée : {e}")

    # ── Création de compte ────────────────────────────────────────────────
    with tab_signup:
        email = st.text_input("Email", key="signup_email")
        pwd   = st.text_input("Mot de passe", type="password", key="signup_pwd")

        if st.button("Créer un compte"):
            try:
                supabase.auth.sign_up(
                    {
                        "email": email,
                        "password": pwd,
                        "options": {
                            "email_redirect_to": f"{SITE_URL}/?confirm",
                        },
                    }
                )
                st.session_state.pending_confirmation = True
                st.success("✅ Compte créé ! Vérifie ta boîte mail.")
            except Exception as e:
                st.error(f"❌ Erreur d'inscription : {e}")

# ── LOGOUT ────────────────────────────────────────────────────────────────
def logout() -> None:
    for key in ["authenticated", "user", "token"]:
        st.session_state.pop(key, None)
    st.rerun()

# ── CHECK SESSION ─────────────────────────────────────────────────────────
def check_session() -> bool:
    return st.session_state.get("authenticated", False)