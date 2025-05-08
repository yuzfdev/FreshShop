import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres.tclbwjgjvdrenalrdvbx",
        password="Jjsh@5371",  # ← Replace with your actual password
        host="aws-0-ap-south-1.pooler.supabase.com",
        port="5432",
    )
    print("✅ Successfully connected to the database!")
except Exception as e:
    print("❌ Could not connect:", str(e))