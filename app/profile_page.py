import uuid
import streamlit as st
from utils import get_anon_client, get_service_client
from app.auth_supabase import supabase

# Initialisation des clients
db = get_anon_client()
storage = get_service_client()
PROFILE_BUCKET = "avatars"


@st.cache_data(ttl=60)
def get_profile(user_id: str) -> dict:
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


def profile_page() -> None:
    user = st.session_state.get("user")
    if user is None:
        st.error("Non authentifié.")
        return

    profile = get_profile(user.id)

    st.title("👤 Profil collaborateur")
    col_avatar, col_fields = st.columns([1, 3])

    with col_avatar:
        st.image(
            profile.get("avatar_url") or "https://placehold.co/150x150?text=Avatar",
            width=150,
        )
        avatar_file = st.file_uploader(
            "Changer l'avatar (PNG/JPG)",
            type=["png", "jpg", "jpeg"],
            label_visibility="collapsed",
        )

    with col_fields:
        display_name = st.text_input("Nom affiché", profile.get("display_name", ""))
        bio = st.text_area("Bio", profile.get("bio", ""), height=150)
        github_url = st.text_input("Lien GitHub", profile.get("github_url", ""))

    if st.button("💾 Enregistrer les modifications"):
        new_avatar_url = profile.get("avatar_url", "")

        if avatar_file is not None:
            ext = avatar_file.name.split(".")[-1]
            path = f"{user.id}/{uuid.uuid4()}.{ext}"
            data = avatar_file.getvalue()

            storage.storage.from_(PROFILE_BUCKET).upload(
                path,
                data,
                {"content-type": avatar_file.type},
            )
            new_avatar_url = storage.storage.from_(PROFILE_BUCKET).get_public_url(path)

        supabase.table("profiles").update({
            "display_name": display_name,
            "bio": bio,
            "github_url": github_url,
            "avatar_url": new_avatar_url,
        }).eq("id", user.id).execute()

        st.session_state.display_name = display_name
        st.session_state.avatar_url = new_avatar_url
        st.cache_data.clear()
        st.toast("🔥 Avatar enregistré avec succès !", icon="🎉")
        with st.expander("Voir le résultat ?"):
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG42c3ZxMGhtMGt6cTJvZXY0cXRnMTB2cHJyZHR5N3kycmloajgzeCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7abB06u9bNzA8lu8/giphy.gif")