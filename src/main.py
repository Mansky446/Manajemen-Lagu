from re import search
from os import system

import modul.data_lagu as data_lagu

# Mendapatkan dan cek input dari user
def dapatkan_input_dan_cek(pesan, pesan_salah, regex):
    while True:
        print(pesan)
        string_input = input("> ").strip()
        # Jika input sesuai, keluar dari infinite loop
        if search(regex, string_input) is not None:
            return string_input
        print(pesan_salah)

# Untuk menampilkan menu awal
def tampilkan_menu_awal():
    print("Selamat Datang di Manajemen Lagu")
    print("---------------------------------")
    print("1. Tambah lagu")
    print("2. Hapus lagu")
    print("3. Edit lagu")
    print("4. Lihat lagu")
    print("5. Lihat detail lagu")
    print("6. Masuk mode setel lagu")
    print("7. Keluar\n")
    # Mendapatkan input dari user
    opsi = input("Pilih opsi (1-6): ")
    print("")

    try:
        opsi = int(opsi)
    except:
        # Bila input bukan angka, error
        print("Input opsi tidak sesuai!\n")
    else:
        if opsi < 1 or opsi > 6:
            # Bila input tidak diantara 1-6
            print("Masukkan opsi 1-6!\n")
    return opsi

# Untuk menampilkan menu setel lagu
def tampilkan_menu_setel_lagu():
    print("Mode Setel Lagu")
    print("---------------")
    print("1. Putar lagu")
    print("2. Jeda lagu")
    print("3. Mulai kembali lagu")
    print("4. Info lagu yang sedang diputar")
    print("5. Lompat ke detik")
    print("6. Keluar\n")
    # Mendapatkan input dari user
    opsi = input("Pilih opsi (1-6): ")
    print("")

    try:
        opsi = int(opsi)
    except:
        # Bila input bukan angka, error
        print("Input opsi tidak sesuai!\n")
    else:
        if opsi < 1 or opsi > 6:
            # Bila input tidak diantara 1-6
            print("Masukkan opsi 1-6!\n")
    return opsi

def mode_setel_lagu():
    tampilkan_menu_setel_lagu()

# Mode menu awal
def mode_menu_awal():
    while True:
        system("cls")
        opsi = tampilkan_menu_awal()
        # Jika opsi = 1, menembahkan lagu
        if opsi == 1:
            judul = dapatkan_input_dan_cek("Masukkan judul lagu", "Input judul tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            album = dapatkan_input_dan_cek("Masukkan Album lagu", "Input album tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            penyanyi = dapatkan_input_dan_cek("Masukkan penyayi lagu", "Input penyanyi tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            genre = dapatkan_input_dan_cek("Masukkan genre lagu", "Input genre tidak sesuai, harap diulang!", r"^\w[\w\s]*$")
            tahun = dapatkan_input_dan_cek("Masukkan tahun lagu [tttt]", "Input tahun tidak sesuai, harap diulang!", r"^[0-9]{4}$")
            durasi = dapatkan_input_dan_cek("Masukkan durasi lagu [mm:dd]", "Input durasi tidak sesuai, harap diulang!", r"^[0-9]{2}:[0-9]{2}$")
            print("")

            if data_lagu.tambah_lagu(judul, penyanyi, album, genre, tahun, durasi):
                print(f"Lagu {judul} berhasil ditambahkan\n")
            else:
                print(f"Lagu {judul} sudah ada\n")
        # Jika opsi = 2, hapus lagu
        elif opsi == 2:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini\n")
            else:
                print("Masukkan judul lagu yang ingin dihapus")
                judul = input("> ").strip()
                print("")

                if data_lagu.hapus_lagu(judul):
                    print(f"Lagu {judul} berhasil dihapus\n")
                else:
                    print(f"Lagu {judul} tidak ditemukan\n")
        # Jika opsi = 3, edit lagu
        elif opsi == 3:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini\n")
            else:
                print("Masukkan judul lagu yang ingin diedit")
                judul = input("> ").strip()
                print("")

                lagu = data_lagu.dapatkan_lagu(judul)

                if lagu is None:
                    print(f"Lagu {judul} tidak ditemukan\n")
                else:
                    judul = dapatkan_input_dan_cek("Masukkan judul lagu (Kosongkan bila tidak ingin diubah)", "Input judul tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$")
                    album = dapatkan_input_dan_cek("Masukkan Album lagu (Kosongkan bila tidak ingin diubah)", "Input album tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$")
                    penyanyi = dapatkan_input_dan_cek("Masukkan penyayi lagu (Kosongkan bila tidak ingin diubah)", "Input penyanyi tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$")
                    genre = dapatkan_input_dan_cek("Masukkan genre lagu (Kosongkan bila tidak ingin diubah)", "Input genre tidak sesuai, harap diulang!", r"^$|^\w[\w\s]*$")
                    tahun = dapatkan_input_dan_cek("Masukkan tahun lagu [tttt] (Kosongkan bila tidak ingin diubah)", "Input tahun tidak sesuai, harap diulang!", r"^$|^[0-9]{4}$")
                    durasi = dapatkan_input_dan_cek("Masukkan durasi lagu [mm:dd] (Kosongkan bila tidak ingin diubah)", "Input durasi tidak sesuai, harap diulang!", r"^$|^[0-9]{2}:[0-9]{2}$")
                    print("")

                    list_properti_yang_diedit = data_lagu.edit_lagu(lagu, judul, penyanyi, album, genre, tahun, durasi)

                    if list_properti_yang_diedit is None:
                        print(f"Data lagu {lagu["judul"]} tidak ada yang diubah\n")
                    else:
                        for properti_yang_diedit in list_properti_yang_diedit:
                            print(f"{properti_yang_diedit["tipe"].capitalize()} lagu berhasil diubah, {properti_yang_diedit["data_sebelumnya"]} -> {properti_yang_diedit["data_baru"]}")
                        print("")
        # Jika opsi = 4, lihat semua lagu
        elif opsi == 4:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini\n")
            else:
                print("Daftar Lagu:")
                print("------------")
                data_lagu.print_semua_lagu("judul")
                print("")
        # Jika opsi = 5, lihat detail lagu
        elif opsi == 5:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini\n")
            else:
                print("Masukkan judul lagu yang ingin dilihat detailnya")
                judul = input("> ").strip()
                print("")

                lagu = data_lagu.dapatkan_lagu(judul)

                if lagu is None:
                    print(f"Lagu {judul} tidak ditemukan\n")
                else:
                    print(f"Detail Lagu {judul}:")
                    print("-------------" + '-' * len(judul))
                    data_lagu.print_detail_lagu(lagu)
                    print("")
        # Jika opsi = 6, masuk mode setel lagu
        elif opsi == 6:
            mode_setel_lagu()
        # Jika opsi = 6, keluar dari progrsam
        elif opsi == 7:
            data_lagu.keluar()
            print("Anda keluar dari program!\n")
            break
        
        input("Tekan enter untuk melanjutkan ")

# Awal program
if __name__ == "__main__":
    # Inisiasi data lagu
    data_lagu.inisiasi()
    mode_menu_awal()
