from re import search
from os import system

import modul.data_lagu as data_lagu

def dapatkan_input_dan_cek(pesan, pesan_salah, regex):
    while True:
        print(pesan)
        string_input = input("> ").strip()

        if search(regex, string_input) is not None:
            return string_input
        
        print(pesan_salah)

def tampilkan_menu():
    print("Selamat Datang di Manajemen Lagu")
    print("---------------------------------")
    print("1. Tambah lagu")
    print("2. Hapus lagu")
    print("3. Edit lagu")
    print("4. Lihat lagu")
    print("5. Lihat detail lagu")
    print("6. Keluar")
    print("")

    opsi = input("Pilih opsi (1-6): ")
    print("")

    try:
        opsi = int(opsi)
    
    except:
        print("Input opsi tidak sesuai!")
        print("")
    
    else:
        if opsi < 1 or opsi > 6:
            print("Masukkan opsi 1-6!")
            print("")
    
    return opsi


if __name__ == "__main__":
    data_lagu.inisiasi()

    while True:
        system("cls")
        opsi = tampilkan_menu()
        
        if opsi == 1:
            judul = dapatkan_input_dan_cek("Masukkan judul lagu", "Input judul tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            album = dapatkan_input_dan_cek("Masukkan Album lagu", "Input album tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            penyanyi = dapatkan_input_dan_cek("Masukkan penyayi lagu", "Input penyanyi tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            genre = dapatkan_input_dan_cek("Masukkan genre lagu", "Input genre tidak sesuai, harap diulang!", r"^\w[\w\s]*$")
            tahun = dapatkan_input_dan_cek("Masukkan tahun lagu [tttt]", "Input tahun tidak sesuai, harap diulang!", r"^[0-9]{4}$")
            durasi = dapatkan_input_dan_cek("Masukkan durasi lagu [mm:dd]", "Input durasi tidak sesuai, harap diulang!", r"^[0-9]{2}:[0-9]{2}$")
            print("")

            if data_lagu.tambah_lagu(judul, penyanyi, album, genre, tahun, durasi):
                print(f"Lagu {judul} berhasil ditambahkan")
                print("")

            else:
                print(f"Lagu {judul} sudah ada")
                print("")
            
        elif opsi == 2:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Masukkan judul lagu yang ingin dihapus")
                judul = input("> ").strip()
                print("")

                if data_lagu.hapus_lagu(judul):
                    print(f"Lagu {judul} berhasil dihapus")
                    print("")
                
                else:
                    print(f"Lagu {judul} tidak ditemukan")
                    print("")
        
        elif opsi == 3:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Masukkan judul lagu yang ingin diedit")
                judul = input("> ").strip()
                print("")

                lagu = data_lagu.dapatkan_lagu(judul)

                if lagu is None:
                    print(f"Lagu {judul} tidak ditemukan")
                    print("")

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
                        print(f"Data lagu {lagu["judul"]} tidak ada yang diubah")
                        print("")

                    else:
                        for properti_yang_diedit in list_properti_yang_diedit:
                            print(f"{properti_yang_diedit["tipe"].capitalize()} lagu berhasil diubah, {properti_yang_diedit["data_sebelumnya"]} -> {properti_yang_diedit["data_baru"]}")
                        
                        print("")
        
        elif opsi == 4:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Daftar Lagu:")
                print("------------")

                data_lagu.print_semua_lagu("judul")
                print("")
        
        elif opsi == 5:
            if data_lagu.apakah_lagu_kosong():
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Masukkan judul lagu yang ingin dilihat detailnya")
                judul = input("> ").strip()
                print("")

                lagu = data_lagu.dapatkan_lagu(judul)

                if lagu is None:
                    print(f"Lagu {judul} tidak ditemukan")
                    print("")
                
                else:
                    print(f"Detail Lagu {judul}:")
                    print("-------------" + '-' * len(judul))

                    data_lagu.print_detail_lagu(lagu)
                    print("")
        
        elif opsi == 6:
            data_lagu.keluar()
            print("Anda keluar dari program!")
            print("")
            break

        input("Tekan enter untuk melanjutkan ")
