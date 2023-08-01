from datetime import datetime
a = datetime.now()

print("Selamat Datang Di Database Sederhana v 1.0")
print("  ")
print("Sekarang {}".format(a))
print("   ")
print("Silahkan Pilih Menu")

def menu():
    print("[0] Lihat Tabel")
    print("[1] Tambah Row Tabel")
    print("[2] Hapus Row Tabel")
    print("[3] Setup Tabel")
    print("[4] Tentang")
    print("[5] Keluar")
    
menu()

opsi = int(input("Input Anda: "))

if opsi == 0:
    exec(open("list.py").read())
if opsi == 1:
    exec(open("tambah.py").read())
if opsi == 2:
    exec(open("hapus.py").read())
if opsi == 3:
    exec(open("setup.py").read())
if opsi == 4:
    exec(open("about.py").read())
if opsi == 5:
    print("Selamat Tinggal ^^")