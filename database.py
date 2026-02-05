import sqlite3
from sqlite3 import IntegrityError


DB_PATH = "data/urls.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def insert_url(original_url):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO urls (original_url) VALUES (?)",
        (original_url,)
    )
    
    conn.commit()
    url_id = cursor.lastrowid
    conn.close()
    
    return url_id


def save_short_code(url_id, short_code):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE urls SET short_code = ? WHERE id = ?",
        (short_code, url_id)
    )
    
    conn.commit()
    conn.close()