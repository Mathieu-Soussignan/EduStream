import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL       = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY  = os.getenv("SUPABASE_ANON_KEY") or os.getenv("SUPABASE_KEY")
SUPABASE_SR_KEY    = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("❌ SUPABASE_URL et/ou SUPABASE_ANON_KEY manquantes")

anon_client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
if not SUPABASE_SR_KEY:
    raise RuntimeError("❌ SUPABASE_SERVICE_ROLE_KEY manquante")
service_client = create_client(SUPABASE_URL, SUPABASE_SR_KEY)


def get_anon_client():
    return anon_client


def get_service_client():
    return service_client