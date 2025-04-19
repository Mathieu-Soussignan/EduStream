"""Page Streamlit : Profil collaborateur
------------------------------------------------
Fonctionnalités :
• Voir / modifier display_name, bio, lien GitHub
• Téléverser un avatar (bucket Supabase "avatars")
"""

import uuid
import streamlit as st
from utils import get_anon_client, get_service_client

# ────────────────────────────────────────────────────────────────────────────────
# Initialisation des clients Supabase
# ────────────────────────────────────────────────────────────────────────────────
db = get_anon_client()     # pour SELECT / UPDATE profiles (RLS)
storage = get_service_client()  # pour l’upload d’avatars (bypass RLS)

PROFILE_BUCKET = "avatars"


# ──────────────────────────────────────
@st.cache_data(ttl=60)
def get_profile(user_id: str) -> dict:
    """
    Retourne le profil ou un dict vierge.
    Pas d’INSERT ici : le trigger + SQL manuel gèrent la création.
    """
    resp = (
        db.table("profiles")
        .select("display_name,bio,avatar_url,github_url,role")
        .eq("id", user_id)
        .execute()
    )
    rows = resp.data or []
    return rows[0] if rows else {
        "display_name": "",
        "bio": "",
        "github_url": "",
        "avatar_url": "",
        "role": "user",
    }


# ──────────────────────────────────────────
def profile_page() -> None:
    """Affiche / édite le profil courant."""
    user = st.session_state.get("user")
    if user is None:
        st.error("Non authentifié.")
        return

    profile = get_profile(user.id)

    st.title("👤 Profil collaborateur")
    col_avatar, col_fields = st.columns([1, 3])

    # ── Avatar ──────────────────────────────
    with col_avatar:
        st.image(
            profile.get("avatar_url")
            or "https://placehold.co/150x150?text=Avatar",
            width=150,
        )
        avatar_file = st.file_uploader(
            "Changer l'avatar (PNG/JPG)",
            type=["png", "jpg", "jpeg"],
            label_visibility="collapsed",
        )

    # ── Champs texte ──────────────────────────
    with col_fields:
        display_name = st.text_input(
            "Nom affiché",
            profile.get("display_name", ""),
        )
        bio = st.text_area(
            "Bio",
            profile.get("bio", ""),
            height=150,
        )
        github_url = st.text_input(
            "Lien GitHub",
            profile.get("github_url", ""),
        )

    # ── Enregistrer ────────────────────────────
    if st.button("💾 Enregistrer les modifications"):
        new_avatar_url = profile.get("avatar_url", "")

        # 1) Upload avatar via SERVICE ROLE (bypass RLS)
        if avatar_file is not None:
            ext = avatar_file.name.split(".")[-1]
            path = f"{user.id}/{uuid.uuid4()}.{ext}"
            data = avatar_file.getvalue()
            storage.storage.from_(PROFILE_BUCKET).upload(
                path,
                data,
                {"content-type": avatar_file.type},
            )
            # get_public_url renvoie directement la string URL
            new_avatar_url = storage.storage.from_(PROFILE_BUCKET).get_public_url(path)

        # 2) Update du profil via ANON client (RLS sur profiles)
        db.table("profiles").update({
            "display_name": display_name,
            "bio": bio,
            "github_url": github_url,
            "avatar_url": new_avatar_url,
        }).eq("id", user.id).execute()

        # 3) Sync session & cache
        st.session_state.display_name = display_name
        st.session_state.avatar_url = new_avatar_url
        st.cache_data.clear()
        st.success("Profil mis à jour ✅")

    # ── Rôle (lecture seule) ─────────────────────────────────────────────────
    st.markdown(f"**Rôle** : `{profile.get('role', 'user')}`")