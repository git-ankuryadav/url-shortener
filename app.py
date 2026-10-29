from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

# temp storage
urls = {}

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

    code = generate_code()
    urls[code] = original_url

    short_url = request.host_url + code
    print(urls.items())

    return f"""
        <h2>Your shortened URL:</h2>
        <a href="{short_url}">{short_url}</a>
        <p><a href="/">Shorten another URL</a></p>
    """

@app.route("/<code>")
def redirect_url(code):
    original_url = urls.get(code)

    if original_url:
        return redirect(original_url)

    return "Short URL not found!", 404

if __name__ == "__main__":
    app.run(debug=True)
