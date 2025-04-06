from supabase import create_client, Client
import resend

# --- Supabase setup ---
SUPABASE_URL = "https://psjjznbgktdkhikpodcq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBzamp6bmJna3Rka2hpa3BvZGNxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MzkxMDA4OSwiZXhwIjoyMDU5NDg2MDg5fQ.yrrPIun5DPVKsx-1kk-1WQ7UZwyLF59oRMrpOfaExlQ"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Resend setup ---
resend.api_key = "re_aFQy1Ggq_8WR19y4maWq8n7BEpsntsazo"

def send_email(to_email):
    # if to_email != "ranaakshatyt45@gmail.com":
    #     print(f"⛔ Blocked sending to {to_email} (only allowed to verified address)")
    #     return
    
    response = resend.Emails.send({
        "from": "Akshat <onboarding@resend.dev>",
        "to": [to_email],
        "subject": " Your Daily AI Digest!",
        "html": "<h2>Hey there!</h2><p>This is your daily update from AIgen 🚀</p>",
    })
    print(f"📤 Sent to {to_email}: {response['id']}")

def fetch_users():
    result = supabase.table("users").select("email").execute()
    users = result.data
    for user in users:
        print(f"📬 Found: {user['email']}")
        send_email(user['email'])

if __name__ == "__main__":
    fetch_users()
