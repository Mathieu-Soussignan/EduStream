from unittest.mock import MagicMock, patch
import streamlit as st
import pytest

from app.profile_page import get_profile


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
    result = get_profile("123")
    assert isinstance(result, dict)
    assert result["avatar_url"] == ""
    assert result["role"] == "user"


def test_get_profile_found(monkeypatch):
    """Teste le cas où un profil est trouvé."""
    fake_data = [{
        "display_name": "Toto",
        "bio": "Test bio",
        "avatar_url": "http://example.com/avatar.png",
        "github_url": "https://github.com/toto",
        "role": "user"
    }]

    class FakeTable:
        def select(self, *args): return self
        def eq(self, *args): return self
        def execute(self):
            class R: data = fake_data
            return R()

    fake_db = type("DB", (), {"table": lambda self, t: FakeTable()})()
    monkeypatch.setattr("app.profile_page.db", fake_db)
    result = get_profile("123")
    assert result["display_name"] == "Toto"


def test_profile_update(monkeypatch):
    """Teste que l'update du profil est bien appelé avec les bons champs."""
    fake_user = MagicMock()
    fake_user.id = "user-xyz"
    st.session_state.user = fake_user
    st.session_state.display_name = "Old Name"

    fake_supabase = MagicMock()
    monkeypatch.setattr("app.profile_page.supabase", fake_supabase)

    with patch("streamlit.st") as mock_st:
        mock_st.session_state = st.session_state
        mock_st.file_uploader.return_value = None
        mock_st.text_input.side_effect = ["New Name"]
        mock_st.text_area.return_value = "Updated bio"
        mock_st.text_input.return_value = "https://github.com/user"
        mock_st.button.return_value = True

        from app.profile_page import profile_page
        profile_page()

        args, kwargs = fake_supabase.table().update.call_args
        assert "display_name" in args[0]
        assert args[0]["display_name"] == "New Name"