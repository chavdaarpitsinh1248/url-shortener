from flask import Flask, request, jsonify
from models import create_tables
from database import insert_url, save_short_code
from shortener import encode_base62


app = Flask(__name__)


@app.route("/")
def home():
    return "URL Shortener is Running"


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    
    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400
    
    original_url = data["url"]
    
    # Step 1: Insert URL
    url_id = insert_url(original_url)
    
    # Step 2: Generate short code
    short_code = encode_base62(url_id)
    
    # Step 3: Save short code
    save_short_code(url_id, short_code)
    
    short_url = request.host_url + short_code
    
    return jsonify({"short_url": short_url}), 201

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)