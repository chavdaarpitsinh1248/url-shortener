from flask import Flask
from models import create_tables

app = Flask(__name__)

@app.route("/")
def home():
    return "URL Shortener is Running"

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)