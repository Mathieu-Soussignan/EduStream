import sys
import pytest
import importlib
from unittest.mock import MagicMock
import streamlit as st


def test_get_profile_empty(monkeypatch):
    # ✅ désactive @st.cache_data pour éviter l’erreur Streamlit
    monkeypatch.setattr(st, "cache_data", lambda ttl=None: (lambda f: f))

    # ✅ mock : simulate .data = [{}]
    fake_resp = MagicMock()
    fake_resp.data = [{
        "display_name": "",
        "bio": "",
        "github_url": "",
        "avatar_url": "",
        "role": "user"
    }]

    fake_execute = MagicMock(return_value=fake_resp)
    fake_eq = MagicMock(return_value=MagicMock(execute=fake_execute))
    fake_select = MagicMock(return_value=MagicMock(eq=fake_eq))
    fake_table = MagicMock(return_value=MagicMock(select=fake_select))
    fake_client = MagicMock(table=fake_table)

    sys.modules["utils"] = MagicMock()
    sys.modules["utils.supabase_client"] = MagicMock(get_anon_client=lambda: fake_client)

    sys.modules.pop("app.profile_page", None)
    profile_module = importlib.import_module("app.profile_page")

    profile = profile_module.get_profile("any-user-id")

    # ✅ VÉRIFICATION
    assert isinstance(profile, dict)
    assert profile["role"] == "user"
    assert profile["avatar_url"] == ""