import psycopg2

conn = psycopg2.connect(
    dbname="data",
    user="postgres",
    password="1234",
    host="localhost",
    port="1234"
)
cur = conn.cursor()

cur.execute(
        "DROP TABLE users;"
        )
conn.commit()