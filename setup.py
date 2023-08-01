import sqlite3

# Nama database
db_file = "perpustakaan.sql"

# Koneksi kedalam database
conn: sqlite3.Connection = None
try:
    conn = sqlite3.connect("./" + db_file)
except sqlite3.Error as e:
    print(e)

# Membuat tabel buku
conn.execute("CREATE TABLE buku ("
             "id INTEGER PRIMARY KEY AUTOINCREMENT,"
             "judul TEXT NOT NULL,"
             "deskripsi TEXT NOT NULL"
             ")")

# id adalah nama kolom
# INTEGER adalah tipe data dan INTEGER artinya angka
# PRIMARY KEY digunakan untuk membedakan setiap buku
# AUTOINCREMENT digunakan agar setiap kita menambahkan data, "id" otomatis terisi
# NOT NULL artinya tidak boleh dikosongi

# Tutup koneksi setelah digunakan

print("Setup berhasil, Silahkan buka menu.py")

conn.close()