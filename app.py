from flask import Flask, request, jsonify, redirect, render_template
from models import create_tables
from database import insert_url, save_short_code, get_url_by_code, get_url_by_original, increment_clicks
from shortener import encode_base62
from urllib.parse import urlparse


app = Flask(__name__)

def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])


@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    error = None
    
    if request.method == "POST":
        original_url = request.form.get("url", "").strip()
        
        if not is_valid_url(original_url):
            error = "Please enter a valid URL"
        else:
            existing = get_url_by_original(original_url)
            
            if existing:
                short_url = request.host_url + existing["short_code"]
            else:
                url_id = insert_url(original_url)
                short_code = encode_base62(url_id)
                save_short_code(url_id, short_code)
                short_url = request.host_url + short_code
    
    return render_template("index.html", short_url=short_url, error=error)


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    
    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400
    
    original_url = data["url"].strip()
    
    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400
    
    existing = get_url_by_original(original_url)
    
    if existing:
        short_url = request.host_url + existing["short_code"]
        return jsonify({"short_url": short_url}), 200
    
    # Step 1: Insert URL
    url_id = insert_url(original_url)
    
    # Step 2: Generate short code
    short_code = encode_base62(url_id)
    
    # Step 3: Save short code
    save_short_code(url_id, short_code)
    
    short_url = request.host_url + short_code
    
    return jsonify({"short_url": short_url}), 201


@app.route("/<short_code>")
def redirect_url(short_code):
    url_data = get_url_by_code(short_code)
    
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404
    
    if url_data["expires_at"]:
        return jsonify({"error": "Short URL expired"}), 410
    
    # Increment click count
    increment_clicks(url_data["id"])
    
    return redirect(url_data["original_url"], code=302)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)