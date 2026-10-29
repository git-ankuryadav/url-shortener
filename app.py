from flask import Flask, request, redirect
import random
import string
import sqlite3

app = Flask(__name__)

# temp storage
# urls = {}

DATABASE = "urls.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def generate_code(length = 6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars,k=length))


@app.route('/')
def home():
    return """
    <html>
    <body>
    <h1>URL Shortener</h1>
    <form action="/shorten" method="POST">
        <input type="url" name="url"
               placeholder="Enter your URL" required>
        <button type="submit">Shorten URL</button>
    </form>
    </body>
    </html>
    """

@app.route("/shorten", methods=["POST"])
def shorten():
    original_url = request.form.get("url")

    conn = get_db_connection()

    while True:
        code = generate_code()
        try:
            conn.execute(
                "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
                (code, original_url)
            )
            conn.commit()
            break
        except sqlite3.IntegrityError:
            continue

    conn.close()

    short_url = request.host_url + code

    return f"""
        <h2>Your shortened URL:</h2>
        <a href="{short_url}">{short_url}</a>
        <p><a href="/">Shorten another URL</a></p>
    """


@app.route("/<code>")
def redirect_url(code):
    conn = get_db_connection()

    url = conn.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (code,)
    ).fetchone()

    conn.close()

    if url:
        return redirect(url["original_url"])

    return "Short URL not found!", 404


init_db()

if __name__ == "__main__":
    app.run(debug=True)
