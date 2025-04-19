import sys
import pytest
import importlib
from unittest.mock import MagicMock


def test_get_profile_empty(monkeypatch):
    # ⛔️ on mocke le module utils AVANT d'importer profile_page
    sys.modules["utils"] = MagicMock()

    # créer un faux client avec une table qui retourne rien
    class FakeTable:
        def select(self, *args): return self
        def eq(self, *args): return self
        def execute(self):
            class R: data = []
            return R()
    fake_db = type("FakeClient", (), {"table": lambda self, name: FakeTable()})()

    # on force utils.get_anon_client() à renvoyer notre fake
    sys.modules["utils.supabase_client"] = MagicMock(get_anon_client=lambda: fake_db)

    # importer après avoir patché
    sys.modules.pop("app.profile_page", None)
    profile_module = importlib.import_module("app.profile_page")

    profile = profile_module.get_profile("any-user-id")

    assert isinstance(profile, dict)
    assert profile["role"] == "user"
    assert profile["avatar_url"] == ""