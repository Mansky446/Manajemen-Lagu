import re

list_lagu = []

def dapatkan_index_lagu(judul_lagu):
    jumlah_lagu = len(list_lagu)

    if jumlah_lagu != 0:
        for i in range(jumlah_lagu):
            lagu = list_lagu[i]

            if lagu["judul"] == judul_lagu:
                return i
    
    return -1


def tambah_lagu(judul, penyanyi, album, genre, tahun, durasi):
    if dapatkan_index_lagu(judul) != -1:
        return False
    
    list_lagu.append({
        "judul": judul,
        "penyanyi": penyanyi,
        "album": album,
        "genre": genre,
        "tahun": tahun,
        "durasi": durasi
    })

    return True

def edit_lagu(lagu, judul, penyanyi, album, genre, tahun, durasi):
    data_edit = []

    def edit(tipe, data_baru):
        data_edit.append({ "tipe": tipe, "data_sebelumnya": lagu[tipe], "data_baru" : data_baru})
        lagu["judul"] = data_baru

    if len(judul) != 0: edit("judul", judul)
    if len(penyanyi) != 0: edit("penyanyi", penyanyi)
    if len(album) != 0: edit("album", album)
    if len(genre) != 0: edit("genre", genre)
    if len(tahun) != 0: edit("tahun", tahun)
    if len(durasi) != 0: edit("durasi", durasi)

    return None if len(data_edit) == 0 else data_edit
    
def hapus_lagu(judul):
    index_lagu = dapatkan_index_lagu(judul)

    if index_lagu == -1:
        return False
    
    list_lagu.pop(index_lagu)

    return True

if __name__ == "__main__":
    while True:
        print("")
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
            continue
        else:
            if opsi < 1 and opsi > 6:
                print("Masukkan opsi 1-6!")
                print("")
                continue
        
        if opsi == 1:
            def dapatkan_input_dan_cek(pesan, pesan_salah, regex):
                while True:
                    print(pesan)
                    string_input = input("> ").strip()

                    if re.search(regex, string_input) is not None:
                        return string_input
                    
                    print(pesan_salah)

            judul = dapatkan_input_dan_cek("Masukkan judul lagu", "Input judul tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            album = dapatkan_input_dan_cek("Masukkan Album lagu", "Input album tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            penyanyi = dapatkan_input_dan_cek("Masukkan penyayi lagu", "Input penyanyi tidak sesuai, harap diulang!", r"^\w[\w\s']*$")
            genre = dapatkan_input_dan_cek("Masukkan genre lagu", "Input genre tidak sesuai, harap diulang!", r"^\w[\w\s]*$")
            tahun = dapatkan_input_dan_cek("Masukkan tahun lagu [tttt]", "Input tahun tidak sesuai, harap diulang!", r"^[0-9]{4}$")
            durasi = dapatkan_input_dan_cek("Masukkan durasi lagu [mm:dd]", "Input durasi tidak sesuai, harap diulang!", r"^[0-9]{2}:[0-9]{2}$")
            print("")

            if tambah_lagu(judul, penyanyi, album, genre, tahun, durasi):
                print("Lagu %s berhasil ditambahkan" % (judul))
                print("")

            else:
                print("Lagu %s sudah ada" % (judul))
                print("")
            
        elif opsi == 2:
            if len(list_lagu) == 0:
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Masukkan judul lagu yang ingin dihapus")
                judul = input("> ").strip()
                print("")

                if hapus_lagu(judul):
                    print("Lagu %s sudah berhasil dihapus" % (judul))
                    print("")
                
                else:
                    print("Lagu %s tidak ditemukan" % (judul))
                    print("")
        
        elif opsi == 3:
            if len(list_lagu) == 0:
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Masukkan judul lagu yang ingin diedit")
                judul = input("> ").strip()
                print("")

                index_lagu = dapatkan_index_lagu(judul)

                if index_lagu == -1:
                    print("Lagu %s tidak ditemukan" % (judul))
                    print("")

                else:
                    def dapatkan_input_dan_cek(pesan, pesan_salah, regex):
                        while True:
                            print(pesan)
                            string_input = input("> ").strip()

                            if re.search(regex, string_input) is not None:
                                return string_input
                            
                            print(pesan_salah)
                    
                    judul = dapatkan_input_dan_cek("Masukkan judul lagu (Kosongkan bila tidak ingin diubah)", "Input judul tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$")
                    album = dapatkan_input_dan_cek("Masukkan Album lagu (Kosongkan bila tidak ingin diubah)", "Input album tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$")
                    penyanyi = dapatkan_input_dan_cek("Masukkan penyayi lagu (Kosongkan bila tidak ingin diubah)", "Input penyanyi tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$")
                    genre = dapatkan_input_dan_cek("Masukkan genre lagu (Kosongkan bila tidak ingin diubah)", "Input genre tidak sesuai, harap diulang!", r"^$|^\w[\w\s]*$")
                    tahun = dapatkan_input_dan_cek("Masukkan tahun lagu [tttt] (Kosongkan bila tidak ingin diubah)", "Input tahun tidak sesuai, harap diulang!", r"^$|^[0-9]{4}$")
                    durasi = dapatkan_input_dan_cek("Masukkan durasi lagu [mm:dd] (Kosongkan bila tidak ingin diubah)", "Input durasi tidak sesuai, harap diulang!", r"^$|^[0-9]{2}:[0-9]{2}$")
                    print("")

                    data_edit = edit_lagu(list_lagu[index_lagu], judul, penyanyi, album, genre, tahun, durasi)

                    if len(data_edit) == 0:
                        print("Data lagu %s tidak ada yang diubah" % (judul))
                        print("")

                    else:
                        for data in data_edit:
                            print("Data %s lagu berhasil diubah %s -> %s" % (data["tipe"], data["data_sebelumnya"], data["data_baru"]))
                        
                        print("")
        
        elif opsi == 4:
            if len(list_lagu) == 0:
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Daftar Lagu:")
                print("------------")

                lagu_terurut = []
                lagu_terurut.extend(list_lagu)
                lagu_terurut.sort(key = lambda elem: elem["judul"])

                urutan_ke = 1

                for lagu in list_lagu:
                    print("%i. %s, %s (%s)" % (urutan_ke, lagu["judul"], lagu["penyanyi"], lagu["durasi"]))
                    urutan_ke += 1

                print("")
        
        elif opsi == 5:
            if len(list_lagu) == 0:
                print("Belum ada lagu untuk saat ini")
                print("")
            
            else:
                print("Masukkan judul lagu yang ingin dilihat detailnya")
                judul = input("> ").strip()
                print("")

                index_lagu = dapatkan_index_lagu(judul)

                if index_lagu == -1:
                    print("Lagu %s tidak ditemukan" % (judul))
                    print("")
                
                else:
                    lagu = list_lagu[index_lagu]

                    print("Detail Lagu '%s':" % (lagu["judul"]))
                    print("---------------" + '-' * len(lagu["judul"]))
                    print("Judul : %s" % (lagu["judul"]))
                    print("Penyanyi : %s" % (lagu["penyanyi"]))
                    print("Album : %s" % (lagu["album"]))
                    print("Genre : %s" % (lagu["genre"]))
                    print("Tahun : %s" % (lagu["tahun"]))
                    print("Durasi : %s" % (lagu["durasi"]))
                    print("")
        
        elif opsi == 6:
            print("Anda keluar dari program!")
            print("")
            break

        input("Tekan enter untuk melanjutkan")
