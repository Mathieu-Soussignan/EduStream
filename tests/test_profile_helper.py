import sys
import pytest
import importlib
from unittest.mock import MagicMock
import streamlit as st


def test_get_profile_empty(monkeypatch):
    # 🧹 Patch le décorateur cache_data pour qu’il retourne la fonction brute
    monkeypatch.setattr(st, "cache_data", lambda ttl=None: (lambda f: f))

    # 👻 Mock utils.get_anon_client pour éviter les dépendances externes
    sys.modules["utils"] = MagicMock()
    sys.modules["utils.supabase_client"] = MagicMock(get_anon_client=lambda: MagicMock(
        table=lambda name: MagicMock(
            select=lambda *args: MagicMock(
                eq=lambda *args: MagicMock(
                    execute=lambda: MagicMock(data=[])
                )
            )
        )
    ))

    # 🔁 Recharger le module après mocks
    sys.modules.pop("app.profile_page", None)
    profile_module = importlib.import_module("app.profile_page")

    profile = profile_module.get_profile("fake-id")
    assert isinstance(profile, dict)
    assert profile["role"] == "user"
    assert profile["avatar_url"] == ""