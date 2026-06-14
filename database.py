import sqlite3
import os

DATABASE = 'youtube_clone.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("Database initialized successfully.")