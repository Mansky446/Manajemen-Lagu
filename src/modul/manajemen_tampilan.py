from modul.utilitas import dapatkan_opsi, dapatkan_input_dan_cek, apakah_file_ada, format_lokasi_file, format_lokasi_absolute

class ManajemenTampilan:
    def __init__(self, manajemen_lagu, pemutar_lagu):
        self.tampilan_aktif = "Menu Awal"
        self.manajemen_lagu = manajemen_lagu
        self.pemutar_lagu = pemutar_lagu
    
    # Fungsi tampilan menu awal
    def menu_awal(self):
        print("Menu Awal")
        print("---------")
        print("1. Manajemen lagu")
        print("2. Pemutar lagu")
        print("3. Keluar program\n")
        opsi = dapatkan_opsi(1, 3, "Pilih menu", "Input tidak valid", "Masukkan input yang sesuai!")
        # Opsi berpindah ke menu manajemen lagu
        if opsi == 1:
            self.tampilan_aktif = "Manajemen Lagu"
            print("\nMasuk ke menu manajemen lagu")
        # Opsi berpindah ke menu pemutar lagu
        if opsi == 2:
            self.tampilan_aktif = "Pemutar Lagu"
            print("\nMasuk ke menu pemutar lagu")
        # Opsi keluar dari program
        elif opsi == 3:
            self.tampilan_aktif = "Keluar"
            print("\nAnda keluar dari program")
    
    # Fungsi tampilan menu manajemen lagu
    def menu_manajemen_lagu(self):
        print("Menu Manajemen Lagu")
        print("-------------------")
        print("1. Tambah lagu")
        print("2. Lihat semua lagu")
        print("3. Lihat detail lagu")
        print("4. Keluar")

        opsi = -1
        # Kalau tidak ada lagu yang diputar, tampilkan opsi 5 dan 6
        if self.pemutar_lagu.dapatkan_lagu_diputar() is None:
            print("5. Hapus lagu")
            print("6. Edit lagu\n")
            opsi = dapatkan_opsi(1, 6, "Pilih opsi", "Input tidak valid", "Masukkan input yang sesuai!")
        
        else:
            opsi = dapatkan_opsi(1, 4, "\nPilih opsi", "Input tidak valid", "Masukkan input yang sesuai!")
        # Opsi tambah lagu
        if opsi == 1:
            print("")
            # Dapatkan input dari user dan cek apakah sudah sesuai
            # Semua properti bisa dikosongkan kecuali judul
            judul = dapatkan_input_dan_cek("Masukkan judul lagu", "Input judul tidak sesuai, harap diulang!", r"^\w[\w\s']*$").strip()
            album = dapatkan_input_dan_cek("Masukkan Album lagu", "Input album tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$").strip()
            penyanyi = dapatkan_input_dan_cek("Masukkan penyayi lagu", "Input penyanyi tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$").strip()
            genre = dapatkan_input_dan_cek("Masukkan genre lagu", "Input genre tidak sesuai, harap diulang!", r"^$|^\w[\w\s/]*$").strip()
            tahun = dapatkan_input_dan_cek("Masukkan tahun lagu [tttt]", "Input tahun tidak sesuai, harap diulang!", r"^$|^[0-9]{4}$").strip()
            lokasi = dapatkan_input_dan_cek("Masukkan lokasi file lagu", "Input lokasi lagu tidak sesuai, harap diulang!", r"^$|^[\w\.][\w\s_\-/\.]*$").strip()
            # Pengecekan string lokasi file
            if len(lokasi) > 0:
                lokasi = format_lokasi_file(lokasi.strip())
                lokasiabs = format_lokasi_absolute(lokasi)
                # Batalkan operasi jika file lagu tidak ditemukan
                if not apakah_file_ada(lokasiabs):
                    print(f"\nFile {lokasi} tidak ada")
                    return
            # Tambahkan lagu dan print laporan
            self.manajemen_lagu.tambah(judul, album, penyanyi, genre, tahun, lokasi)
            print(f"\nLagu '{judul}' berhasil ditambahkan")
        # Opsi lihat semua lagu
        elif opsi == 2:
            # Bila lagu kosong
            if self.manajemen_lagu.apakah_lagu_kosong():
                print("\nSaat ini belum ada lagu")
                return
            
            self.manajemen_lagu.print_semua_lagu(False)
        # Opsi lihat detail lagu
        elif opsi == 3:
            # Bila lagu kosong
            if self.manajemen_lagu.apakah_lagu_kosong():
                print("\nSaat ini belum ada lagu")
                return
            # Dapatkan lagu yang dipilih dari input user berbentuk int index_lagu
            self.manajemen_lagu.print_semua_lagu(True)
            index_lagu = dapatkan_opsi(1, self.manajemen_lagu.dapatkan_total_lagu(), "\nPilih lagu yang ingin dilihat detailnya", "Input tidak valid", "Masukkan input yang sesuai!")
            if index_lagu == -1: return

            lagu = self.manajemen_lagu.dapatkan(index_lagu - 1)

            print(f"\nDetail lagu '{lagu.judul}':")
            print("---------------" + "-" * len(lagu.judul))
            lagu.print_detail()
        # Opsi keluar menu
        elif opsi == 4:
            print("\nAnda keluar dari menu manajemen lagu")
            self.tampilan_aktif = "Menu Awal"
        # Opsi hapus lagu, hanya muncul jika lagutidak ada yang diputar
        elif opsi == 5:
            # Bila lagu kosong
            if self.manajemen_lagu.apakah_lagu_kosong():
                print("\nSaat ini belum ada lagu")
                return
            # Dapatkan lagu yang dipilih dari input user berbentuk int index_lagu
            self.manajemen_lagu.print_semua_lagu(True)
            index_lagu = dapatkan_opsi(1, self.manajemen_lagu.dapatkan_total_lagu(), "\nPilih lagu yang ingin dihapus", "Input tidak valid", "Masukkan input yang sesuai!")
            if index_lagu == -1: return

            lagu = self.manajemen_lagu.dapatkan(index_lagu - 1)
            self.manajemen_lagu.hapus(lagu)

            print(f"\nLagu '{lagu.judul}' berhasil dihapus")
        # Opsi edit lagu, hanya muncul jika lagutidak ada yang diputar
        elif opsi == 6:
            # Bila lagu kosong
            if self.manajemen_lagu.apakah_lagu_kosong():
                print("\nSaat ini belum ada lagu")
                return
            # Dapatkan lagu yang dipilih dari input user berbentuk int index_lagu
            self.manajemen_lagu.print_semua_lagu(True)
            index_lagu = dapatkan_opsi(1, self.manajemen_lagu.dapatkan_total_lagu(), "\nPilih lagu yang ingin diedit", "Input tidak valid", "Masukkan input yang sesuai!")
            if index_lagu == -1: return

            print("")
            # Dapatkan input dari user dan cek apakah sudah sesuai
            # Input bisa dikosongkan bila tidak ingin diubah
            judul = dapatkan_input_dan_cek("Masukkan judul lagu baru", "Input judul tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$").strip()
            album = dapatkan_input_dan_cek("Masukkan Album lagu baru", "Input album tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$").strip()
            penyanyi = dapatkan_input_dan_cek("Masukkan penyayi lagu baru", "Input penyanyi tidak sesuai, harap diulang!", r"^$|^\w[\w\s']*$").strip()
            genre = dapatkan_input_dan_cek("Masukkan genre lagu baru", "Input genre tidak sesuai, harap diulang!", r"^$|^\w[\w\s/]*$").strip()
            tahun = dapatkan_input_dan_cek("Masukkan tahun lagu baru [tttt]", "Input tahun tidak sesuai, harap diulang!", r"^$|^[0-9]{4}$").strip()
            lokasi = dapatkan_input_dan_cek("Masukkan lokasi file lagu baru", "Input lokasi lagu tidak sesuai, harap diulang!", r"^$|^[\w\.][\w\s_\-/\.]*$").strip()
            # Pengecekan string lokasi file
            if len(lokasi) > 0:
                lokasi = format_lokasi_file(lokasi)
                lokasiabs = format_lokasi_absolute(lokasi)
                # Lokasi file tidak jadi diubah jika lokasi file baru tidak ditemukan
                if not apakah_file_ada(lokasiabs):
                    print(f"\nFile {lokasi} tidak ada")
                    lokasi = ""
            
            lagu = self.manajemen_lagu.dapatkan(index_lagu - 1)
            list_properti = [
                ("judul", judul), ("album", album), ("penyanyi", penyanyi),
                ("genre", genre), ("tahun", tahun), ("lokasi", lokasi)
            ]
            # Panggil fungsi untuk mengedit properti
            # Fungsi tersebut mengembalikan list data yang bertipe tuple (nama properti, nilai awal, nilai baru)
            # Bila tidak ada properti diubah, fungsi tersebut mengembalikan list kosong
            list_properti = self.manajemen_lagu.edit(lagu, list_properti)

            if len(list_properti) == 0:
                print(f"\nProperti lagu '{lagu.judul}' tidak ada yang diedit")
                return
            # Print properti yang diubah
            print(f"\nList properti lagu '{lagu.judul}' yang diedit:")
            # Unpack tuple (nama properti, nilai awal, nilai baru)
            for (nama_properti, nilai_awal, nilai_baru) in list_properti:
                print(f"- {nama_properti.capitalize()} lagu diedit, {nilai_awal} -> {nilai_baru}")
    
    # Fungsi tampilan menu pemutar lagu
    def menu_pemutar_lagu(self):
        lagu_diputar = self.pemutar_lagu.dapatkan_lagu_diputar()
        sedang_dijeda = self.pemutar_lagu.apakah_lagu_dijeda()

        print("Menu Pemutar Lagu")
        print("-----------------")
        print("1. Putar lagu" if lagu_diputar is None else "1. Berhenti")
        print("2. Lihat lagu diputar")
        print("3. Keluar")

        opsi = -1
        # Kalau ada lagu yang diputar, tamppilkan opsi 4
        if lagu_diputar is None:
            opsi = dapatkan_opsi(1, 3, "\nPilih opsi", "Input tidak valid", "Masukkan input yang sesuai!")
        
        else:
            print("4. Mulai kembali" if sedang_dijeda else "4. Jeda")
            opsi = dapatkan_opsi(1, 4, "\nPilih opsi", "Input tidak valid", "Masukkan input yang sesuai!")
        # Jika lagu yang diputar selesai sebelum keluar dari fungsi,
        # akan menimbulkan error saat pemanggilan opsi 1, 2 dan 4
        # Keluar dari fungsi untuk mencegah error
        if opsi != 3 and self.pemutar_lagu.dapatkan_lagu_diputar() is not lagu_diputar:
            print(f"\nLagu sudah selesai diputar")
            return
        # Opsi putar lagu
        if opsi == 1:
             # Jika ada lagu yang diputar, opsi 1 adalah behenti
            if lagu_diputar is not None:
                print(f"\nBerhenti memutar lagu '{lagu_diputar.judul}'")
                self.pemutar_lagu.berhenti()
                return
            # Bila lagu kosong
            if self.manajemen_lagu.apakah_lagu_kosong():
                print("\nSaat ini belum ada lagu")
                return
            # Dapatkan lagu dari input
            self.manajemen_lagu.print_semua_lagu(True)
            index_lagu = dapatkan_opsi(1, self.manajemen_lagu.dapatkan_total_lagu(), "\nPilih lagu yang ingin diputar", "Input tidak valid", "Masukkan input yang sesuai!")
            if index_lagu == -1: return

            lagu = self.manajemen_lagu.dapatkan(index_lagu - 1)
            # Batalkan operasi jika lokasi file lagu belum ada
            if lagu.lokasi == "":
                print(f"\nLokasi file lagu '{lagu.judul}' belum ada")
                return
            
            self.pemutar_lagu.mulai(lagu)
            print(f"\nLagu '{lagu.judul}' diputar")
        # Opsi print data lagu yang sedang diputar
        elif opsi == 2:
            # Bila tidak ada lagu yang diputar
            if lagu_diputar is None:
                print("\nBelum ada lagu yang diputar")
                return
            
            self.pemutar_lagu.print_lagu_diputar()
        # Opsi keluar dari menu
        elif opsi == 3:
            print("\nAnda keluar dari menu pemutar lagu")
            self.tampilan_aktif = "Menu Awal"
        # Opsi jeda atau mulai kembali
        elif opsi == 4:
            # Kalau status lagu diputar sedang dijeda, maka opsi 4 adalah mulai kembali
            if sedang_dijeda:
                self.pemutar_lagu.mulai_kembali()
                print(f"\nLagu '{lagu_diputar.judul}' diputar kembali")
                return
            
            self.pemutar_lagu.jeda()
            print(f"\nLagu '{lagu_diputar.judul}' dijeda")
    
    # Fungsi untuk mengatur tampilan mana yang aktif
    def tampilkan(self):
        if self.tampilan_aktif == "Menu Awal":
            self.menu_awal()
        
        elif self.tampilan_aktif == "Manajemen Lagu":
            self.menu_manajemen_lagu()

        elif self.tampilan_aktif == "Pemutar Lagu":
            self.menu_pemutar_lagu()
    
    # Mengembalikan status program, apakah user ingin keluar dari program
    def apakah_keluar(self):
        return self.tampilan_aktif == "Keluar"
