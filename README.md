🔗 URL Shortener — Flask Backend Project

A production-ready URL Shortener built using Python & Flask, similar to bit.ly.
The application converts long URLs into short, shareable links and redirects users while tracking click analytics.

🌐 Live Demo: <[https://url-shortener-0i16.onrender.com/]>

🚀 Features

Shorten long URLs into unique, URL-safe short links

Redirect short URLs to original destinations

Click count tracking for analytics

Input URL validation

Duplicate URL handling (same URL → same short link)

Simple HTML frontend

REST API support

SQLite database persistence

Production deployment using Gunicorn

🛠️ Tech Stack

Language: Python 3

Backend Framework: Flask

Database: SQLite

Web Server: Gunicorn

Deployment: Render

Frontend: HTML + CSS (Flask templates)

📂 Project Structure
url_shortener/
│
├── app.py              # Flask routes and app logic
├── database.py         # Database access layer
├── models.py           # Database schema
├── shortener.py        # Base62 encoding logic
│
├── templates/
│   └── index.html      # Web UI
│
├── data/
│   └── urls.db         # SQLite database (gitignored)
│
├── requirements.txt
├── .gitignore
└── README.md

🔄 How It Works

User submits a long URL

Backend validates the URL

URL is stored in the database

A unique ID is generated

ID is encoded using Base62

Short URL is returned

Visiting the short URL:

Increments click count

Redirects to original URL

🔢 Base62 Encoding

Short URLs are generated using Base62 encoding of the database ID.

Characters used:

0–9 a–z A–Z


This guarantees:

Uniqueness

Short length

URL safety

No collisions

🌐 API Endpoints
➤ Shorten URL

POST /shorten

{
  "url": "https://example.com/very/long/url"
}


Response

{
  "short_url": "https://your-domain/abc123"
}

➤ Redirect

GET /<short_code>

Redirects to the original URL and increments click count.

🖥️ Web Interface

Visit /

Paste a long URL

Click Shorten

Get a clickable short link instantly

⚙️ Local Setup
1️⃣ Clone Repository
git clone https://github.com/chavdaarpitsinh1248/url-shortener.git
cd url-shortener

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application
python app.py


Open browser:

http://127.0.0.1:5000

☁️ Deployment

The application is deployed using Gunicorn on Render.

Production command:

gunicorn app:app

🧠 What This Project Demonstrates

Backend system design

REST API development

Database schema design

URL encoding algorithms

Clean code & refactoring

Deployment & production readiness

📈 Future Improvements

Stats dashboard (/stats/<short_code>)

User authentication

PostgreSQL support

Rate limiting & security hardening

FastAPI migration

Docker support

👤 Author

Chavda Arpitsinh
Aspiring Backend / Python Developer

⭐️ If you like this project

Give it a ⭐ on GitHub — it helps a lot!