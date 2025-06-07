import psycopg2

try:
    conn = psycopg2.connect(
        host="db.zkglooidftewwduzvzsj.supabase.co",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="YOURPASSWORD",
        sslmode="require"
    )
    print("Connected to database successfully!")
    conn.close()
except Exception as e:
    print("Error connecting to database:", e)
