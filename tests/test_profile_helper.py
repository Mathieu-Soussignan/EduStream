import sys
import pytest
import importlib
from unittest.mock import MagicMock
import streamlit as st


def test_get_profile_empty(monkeypatch):
    # ✅ Patch @st.cache_data pour le désactiver en test
    monkeypatch.setattr(st, "cache_data", lambda ttl=None: (lambda f: f))

    # ✅ Mock utils.get_anon_client → retourne un faux client
    fake_execute = MagicMock(return_value=MagicMock(data=[]))  # simule 0 ligne
    fake_eq = MagicMock(return_value=MagicMock(execute=fake_execute))
    fake_select = MagicMock(return_value=MagicMock(eq=fake_eq))
    fake_table = MagicMock(return_value=MagicMock(select=fake_select))
    fake_client = MagicMock(table=fake_table)

    sys.modules["utils"] = MagicMock()
    sys.modules["utils.supabase_client"] = MagicMock(get_anon_client=lambda: fake_client)

    # ❌ Supprime le cache du module pour le recharger proprement
    sys.modules.pop("app.profile_page", None)
    profile_module = importlib.import_module("app.profile_page")

    # ✅ Appel à la fonction patchée
    profile = profile_module.get_profile("any-user-id")

    assert isinstance(profile, dict)
    assert profile["role"] == "user"
    assert profile["avatar_url"] == ""