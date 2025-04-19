import os
from supabase import create_client

# ────────────────────────────────────────────────────────────────────────────────
# Chargement des clés depuis l’environnement
# ────────────────────────────────────────────────────────────────────────────────
SUPABASE_URL               = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY          = os.getenv("SUPABASE_ANON_KEY")
SUPABASE_SERVICE_ROLE_KEY  = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

# ────────────────────────────────────────────────────────────────────────────────
# Validation à l’import (pour que test_missing_env passe)
# ────────────────────────────────────────────────────────────────────────────────
if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("❌ SUPABASE_URL et/ou SUPABASE_ANON_KEY manquantes")
if not SUPABASE_SERVICE_ROLE_KEY:
    raise RuntimeError("❌ SUPABASE_SERVICE_ROLE_KEY manquante")

# ────────────────────────────────────────────────────────────────────────────────
# Création des clients
# ────────────────────────────────────────────────────────────────────────────────
anon_client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
service_client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)


# ────────────────────────────────────────────────────────────────────────────────
# Export des getters
# ────────────────────────────────────────────────────────────────────────────────
def get_anon_client():
    """Client public (ANON key) pour le CRUD RLS sur les tables."""
    return anon_client


def get_service_client():
    """Client service (SERVICE ROLE key) pour bypasser RLS (Storage, functions…)."""
    return service_client