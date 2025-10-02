import sqlite3

DB_NAME = "hrbot.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            skills TEXT NOT NULL,
            experience INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_job(title, skills, experience):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jobs (title, skills, experience) VALUES (?, ?, ?)",
                   (title, skills, experience))
    conn.commit()
    conn.close()

def fetch_jobs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return jobs