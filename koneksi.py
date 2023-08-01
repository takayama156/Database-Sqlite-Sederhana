import sqlite3

# Nama database
db_file = "perpustakaan.sql"

def connect():
    conn: sqlite3.Connection = None
    try:
        conn = sqlite3.connect("./" + db_file)
    except sqlite3.Error as e:
        print(e)
    return conn