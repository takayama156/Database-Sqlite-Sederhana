from koneksi import connect

# Koneksi ke database
conn = connect()

# Mengambil input judul dan deskripsi
print("Tambah buku")
judul = input("Judul : ")
deskripsi = input("Deskripsi : ")

# Menambahkan buku ke tabel buku
cur = conn.cursor()
cur.execute("INSERT INTO buku (judul, deskripsi) VALUES (?, ?)", (judul, deskripsi))
conn.commit()

print("Berhasil menambahkan buku!")