from os import sep

nama_file = f"rawdata{sep}data.txt"

# Inisiasi file, buat file jika file tidak ada
def inisiasi():
    file_ = open(nama_file, "a")
    file_.close()

# Fungsi simpan ke file
def simpan(rawdata):
    file_ = open(nama_file, "w")
    file_.write(rawdata)
    file_.close()

# Fungsi muat dari file
def muat():
    file_ = open(nama_file, "r")
    rawdata = file_.read()
    file_.close()
    return rawdata
