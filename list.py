from tabulate import tabulate
from koneksi import connect

# Koneksi ke database
conn = connect()

# Mengambil data-data buku
cur = conn.cursor()
cur.execute("SELECT * FROM buku")

data = cur.fetchall()

# Mengecek jika data ada (data lebih dari 0)
if len(data) > 0:
    print(tabulate(data, headers=["id", "judul", "deskripsi"]))
else:
    print("Tidak ada data buku!")
    print("Buka tambah.py untuk membuat")