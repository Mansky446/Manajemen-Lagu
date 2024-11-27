from os import sep

nama_file = f"rawdata{sep}data.txt"

def inisiasi():
    file_ = open(nama_file, "a")
    file_.close()

def simpan(rawdata):
    file_ = open(nama_file, "w")
    file_.write(rawdata)
    file_.close()

def muat():
    file_ = open(nama_file, "r")
    rawdata = file_.read()
    return rawdata
