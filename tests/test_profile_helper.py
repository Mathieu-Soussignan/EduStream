import streamlit as st
import pytest
from unittest.mock import MagicMock, patch
import app.profile_page as profile_page


def test_get_profile_empty(monkeypatch):
    """Teste le fallback si aucun profil n'est trouvé dans la base."""
    class FakeTable:
        def select(self, *args): return self
        def eq(self, *args): return self
        def execute(self):
            class R: data = []
            return R()

    fake_db = type("DB", (), {"table": lambda self, t: FakeTable()})()
    monkeypatch.setattr("app.profile_page.db", fake_db)

    result = profile_page.get_profile("00000000-0000-0000-0000-000000000000")
    assert isinstance(result, dict)
    assert result["avatar_url"] == ""
    assert result["role"] == "user"


# def test_get_profile_found(monkeypatch):
#     """Teste le cas où un profil est trouvé."""
#     fake_data = [{
#         "display_name": "Toto",
#         "bio": "Test bio",
#         "avatar_url": "http://example.com/avatar.png",
#         "github_url": "https://github.com/toto",
#         "role": "user"
#     }]

#     class FakeTable:
#         def select(self, *args): return self
#         def eq(self, *args): return self
#         def execute(self):
#             class R: data = fake_data
#             return R()

#     fake_db = type("DB", (), {"table": lambda self, t: FakeTable()})()
#     monkeypatch.setattr("app.profile_page.db", fake_db)

#     result = profile_page.get_profile("00000000-0000-0000-0000-000000000000")
#     assert result["display_name"] == "Toto"


def test_profile_update(monkeypatch):
    """Teste que l'update du profil est bien appelé avec les bons champs."""
    fake_user = MagicMock()
    fake_user.id = "00000000-0000-0000-0000-000000000000"
    st.session_state.user = fake_user
    st.session_state.display_name = "Old Name"

    fake_supabase = MagicMock()
    monkeypatch.setattr("app.profile_page.supabase", fake_supabase)

    with patch("streamlit.file_uploader", return_value=None), \
         patch("streamlit.text_input", side_effect=["New Name", "https://github.com/user"]), \
         patch("streamlit.text_area", return_value="Updated bio"), \
         patch("streamlit.button", return_value=True):

        profile_page.profile_page()

        args, kwargs = fake_supabase.table().update.call_args
        assert "display_name" in args[0]
        assert args[0]["display_name"] == "New Name"