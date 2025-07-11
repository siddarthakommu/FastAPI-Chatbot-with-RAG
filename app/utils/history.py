import sqlite3

DB_PATH = "conversation_history.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS history (user TEXT, message TEXT, response TEXT)")

def save_conversation(user, message, response):
    cursor.execute("INSERT INTO history VALUES (?, ?, ?)", (user, message, response))
    conn.commit()
