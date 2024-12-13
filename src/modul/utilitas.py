from os.path import exists
from os import sep
from re import search

# Konversi int detik ks string durasi mm:ss
def detik_ke_string(detik):
    menit = detik // 60
    sisa_detik = detik - menit * 60
    # Fungsi xfill(2) adalah jika string = "1" maka akan diubah ke "01"
    return (
        f"{str(menit).zfill(2)}:"
        f"{str(sisa_detik).zfill(2)}"
    )

# Konversi string durasi mm:ss ke int detik
def string_ke_detik(string_data):
    # Belah string menjadi list dan ubah lagi menjadi tuple
    # dan lakukan unpack nilai tuple
    (menit, sisa_detik) = tuple(string_data.split(":"))
    return int(menit) * 60 + int(sisa_detik)

# Mengubah "/" (karakter separator) pada string lokasi file ke separator bawaan os
def format_lokasi_file(string_lokasi):
    return string_lokasi.replace("/", sep)

# Mengecek apakah file di lokasi string_lokasi ada atau tidak menggunakan fungsi exists
def apakah_file_ada(string_lokasi):
    return exists(string_lokasi)

# Dapatkan input pilihan atau opsi dari user berbentuk int
def dapatkan_opsi(minimal, maksimal, pesan, pesan_input_tidak_valid, pesan_input_tidak_sesuai):
    print(f"{pesan} [{minimal}-{maksimal}]")
    opsi = input("> ")

    try:
        opsi = int(opsi)
    except:
        # Bila input berisi bukan karakter 0-9
        print(f"\n{pesan_input_tidak_valid}")
        return -1
    else:
        if opsi < minimal or opsi > maksimal:
            # Bila input melewati batas
            print(f"\n{pesan_input_tidak_sesuai}")
            return -1
        # Bila input sesuai
        return opsi

# Dapatkan input dari user dan cek input dengan regex
def dapatkan_input_dan_cek(pesan, pesan_input_tidak_sesuai, pola_regex):
    while True:
        print(pesan)
        string_input = input("> ")
        if search(pola_regex, string_input) is not None:
            # Kalau input sesuai dengan pola regex, keluar dari infinite loop
            return string_input
        
        print(pesan_input_tidak_sesuai)
