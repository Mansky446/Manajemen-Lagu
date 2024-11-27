from datetime import datetime

import modul.file_data as file_data
import modul.format_data as format_data

list_lagu = []

def inisiasi():
    file_data.inisiasi()
    rawdata = file_data.muat()
    
    global list_lagu
    list_lagu = format_data.rawdata_ke_list_lagu(rawdata)

def keluar():
    rawdata = format_data.list_lagu_ke_rawdata(list_lagu)
    file_data.simpan(rawdata)

def apakah_lagu_kosong():
    return len(list_lagu) == 0

def dapatkan_lagu(judul):
    for lagu in list_lagu:

        if lagu["judul"] == judul:
            return lagu
    
    return None

def tambah_lagu(judul, penyanyi, album, genre, tahun, durasi):
    if dapatkan_lagu(judul) is not None:
        return False
    
    list_lagu.append({
        "judul": judul,
        "penyanyi": penyanyi,
        "album": album,
        "genre": genre,
        "tahun": tahun,
        "durasi": durasi,
        "ditambahkan": datetime.now().strftime("%d/%m/%y %H:%M:%S"),
        "diedit": datetime.now().strftime("%d/%m/%y %H:%M:%S")
    })

    return True

def edit_lagu(lagu, judul, penyanyi, album, genre, tahun, durasi):
    data_edit = []

    def edit(tipe, data_baru):
        data_edit.append({ "tipe": tipe, "data_sebelumnya": lagu[tipe], "data_baru" : data_baru})
        lagu[tipe] = data_baru

    if len(judul) != 0: edit("judul", judul)
    if len(penyanyi) != 0: edit("penyanyi", penyanyi)
    if len(album) != 0: edit("album", album)
    if len(genre) != 0: edit("genre", genre)
    if len(tahun) != 0: edit("tahun", tahun)
    if len(durasi) != 0: edit("durasi", durasi)

    if len(data_edit) != 0:
        lagu["diedit"] = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        return data_edit
    
    return None
    
def hapus_lagu(judul):
    lagu = dapatkan_lagu(judul)

    if lagu is None:
        return False
    
    list_lagu.remove(lagu)
    return True

def print_semua_lagu(urut_berdasarkan):
    lagu_terurut = []
    lagu_terurut.extend(list_lagu)
    lagu_terurut.sort(key = lambda lagu: lagu[urut_berdasarkan])

    for index, lagu in enumerate(lagu_terurut):
        print(f"{index + 1}. {lagu["judul"]}, {lagu["penyanyi"]} ({lagu["durasi"]})")

def print_detail_lagu(lagu):
    for properti, nilai in lagu.items():
        if properti == "ditambahkan" or properti == "diedit":
            print(f"{properti.capitalize()} pada: {nilai}")
        
        else:
            print(f"{properti.capitalize()}: {nilai}")
