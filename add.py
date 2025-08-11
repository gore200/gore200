import psycopg2

conn = psycopg2.connect(
    dbname="data",
    user="postgres",
    password="1234",
    host="localhost",
    port="1234"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) UNIQUE,
    pwd VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()