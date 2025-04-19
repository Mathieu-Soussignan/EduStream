import pytest


# on teste la logique de get_profile sans Supabase réel
def test_get_profile_empty(monkeypatch):
    # créer un faux resp.data vide
    class FakeTable:
        def select(self, *args): return self
        def eq(self, *args): return self
        def execute(self):
            class R: data = []
            return R()
    fake_db = type("DB", (), {"table": lambda self, t: FakeTable()})()

    from app.profile_page import get_profile
    # monkeypatch le client global
    import app.profile_page as mod
    monkeypatch.setattr(mod, "db", fake_db)

    profile = get_profile("any-id")
    # sans ligne en base, on attend un dict vierge avec role = user
    assert profile["role"] == "user"
    assert profile["display_name"] == ""