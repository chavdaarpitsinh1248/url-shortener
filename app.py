from flask import Flask, request, jsonify, redirect, render_template
from urllib.parse import urlparse

from models import create_tables
from database import (
    insert_url,
    save_short_code,
    get_url_by_code,
    get_url_by_original,
    increment_clicks,
)
from shortener import encode_base62


app = Flask(__name__)


# --------------------
# Utilities
# --------------------

def is_valid_url(url: str) -> bool:
    """Validate URL structure."""
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


def generate_short_url(original_url: str, host_url: str) -> str:
    """
    Reusable logic to generate or fetch a short URL
    for a given original URL.
    """
    existing = get_url_by_original(original_url)
    if existing:
        return host_url + existing["short_code"]

    url_id = insert_url(original_url)
    short_code = encode_base62(url_id)
    save_short_code(url_id, short_code)

    return host_url + short_code


# --------------------
# Routes
# --------------------

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    error = None

    if request.method == "POST":
        original_url = request.form.get("url", "").strip()

        if not is_valid_url(original_url):
            error = "Please enter a valid URL"
        else:
            short_url = generate_short_url(original_url, request.host_url)

    return render_template(
        "index.html",
        short_url=short_url,
        error=error
    )


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    original_url = data["url"].strip()

    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_url = generate_short_url(original_url, request.host_url)
    return jsonify({"short_url": short_url}), 201


@app.route("/<short_code>")
def redirect_url(short_code):
    url_data = get_url_by_code(short_code)

    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404

    if url_data["expires_at"]:
        return jsonify({"error": "Short URL expired"}), 410

    increment_clicks(url_data["id"])
    return redirect(url_data["original_url"], code=302)


# --------------------
# App bootstrap
# --------------------

create_tables()

if __name__ == "__main__":
    app.run()
