from database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_code TEXT UNIQUE,
        clicks INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()