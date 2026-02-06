import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "urls.db")


# --------------------
# Connection helper
# --------------------

def get_connection():
    """Create and return a SQLite connection."""
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# --------------------
# Write operations
# --------------------

def insert_url(original_url: str) -> int:
    """Insert a new original URL and return its ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO urls (original_url) VALUES (?)",
            (original_url,)
        )
        return cursor.lastrowid


def save_short_code(url_id: int, short_code: str) -> None:
    """Save generated short code for a URL."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE urls SET short_code = ? WHERE id = ?",
            (short_code, url_id)
        )


def increment_clicks(url_id: int) -> None:
    """Increment click counter for a URL."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE urls SET clicks = clicks + 1 WHERE id = ?",
            (url_id,)
        )


# --------------------
# Read operations
# --------------------

def get_url_by_code(short_code: str):
    """Fetch URL row by short code."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM urls WHERE short_code = ?",
            (short_code,)
        )
        return cursor.fetchone()


def get_url_by_original(original_url: str):
    """Fetch URL row by original URL."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM urls WHERE original_url = ?",
            (original_url,)
        )
        return cursor.fetchone()
