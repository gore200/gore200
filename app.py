from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="data",
    user="postgres",
    password="1234",
    host="localhost",
    port="1234"
)
cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    pwd = request.form['pwd']
    cur.execute(
        "INSERT INTO users (username, pwd) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING;", (username, pwd)
        )
    conn.commit()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return render_template('added.html', name=username, count=len(rows))

@app.route('/', methods=['POST'])
def back():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)