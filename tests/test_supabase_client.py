from unittest.mock import MagicMock
import importlib
import pytest
import sys


def test_missing_env(monkeypatch):
    monkeypatch.delenv("SUPABASE_URL", raising=False)
    monkeypatch.delenv("SUPABASE_ANON_KEY", raising=False)
    monkeypatch.delenv("SUPABASE_SERVICE_ROLE_KEY", raising=False)
    sys.modules.pop("utils.supabase_client", None)

    with pytest.raises(RuntimeError) as exc:
        importlib.import_module("utils.supabase_client")

    assert "SUPABASE_URL" in str(exc.value)


def test_load_clients(monkeypatch):
    monkeypatch.setenv("SUPABASE_URL", "https://demo.supabase.co")
    monkeypatch.setenv("SUPABASE_ANON_KEY", "eyJ.fake.anon")
    monkeypatch.setenv("SUPABASE_SERVICE_ROLE_KEY", "eyJ.fake.service")

    # ✅ Patch au bon endroit → supabase.client.create_client
    monkeypatch.setattr("supabase.client.create_client", lambda url, key: MagicMock())

    # Relancer un import propre
    sys.modules.pop("utils.supabase_client", None)
    sc = importlib.import_module("utils.supabase_client")

    anon = sc.get_anon_client()
    svc = sc.get_service_client()
    assert hasattr(anon, "__class__")
    assert hasattr(svc, "__class__")