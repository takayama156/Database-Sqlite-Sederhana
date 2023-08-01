#Memanggil Koneksi.py
from koneksi import connect
  
conn = connect()
print('Masukkan ID!')
  
#Meminta User Memberikan ID Yang Ingin Dihapus
cur = conn.cursor()
id = input()
 
#Melaksanakan Perintah Penghapusan
cur.execute("DElETE FROM Buku WHERE id=?", id)
print('Sukses dihilangkeun sir')
conn.commit()

conn.close()