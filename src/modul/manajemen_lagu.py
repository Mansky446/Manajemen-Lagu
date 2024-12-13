from datetime import datetime
from modul.utilitas import detik_ke_string
from modul.pemutar_lagu import dapatkan_durasi_lagu
from modul.lagu import Lagu

class ManajemenLagu:
    def __init__(self, list_lagu):
        self.list_lagu = list_lagu
    
    # Cek apakah lagu kosong dengan cara membandingkan panjang list_lagu dengan 0
    def apakah_lagu_kosong(self):
        return len(self.list_lagu) == 0
    
    # Dapatkan total lagu dengan cara mendapatkan panjang list_lagu
    def dapatkan_total_lagu(self):
        return len(self.list_lagu)
    
    # Fungsi untuk menambah objek lagu baru ke list_lagu
    def tambah(self, judul, album, penyanyi, genre, tahun, lokasi):
        # Jika user menambahkan lokasi file (lokasi != "") maka update durasi lagu
        # Durasi lagu dinamis sesuai panjang lagu dari file lagu itu sendiri
        durasi = detik_ke_string(dapatkan_durasi_lagu(lokasi)) if lokasi != "" else ""
        # Mendapatkan waktu saat ini dengan format datetime lalu konversi ke string dengan fungsi strftime
        waktu_saat_ini = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        # Buat objek lagu dan tambahkan ke list_lagu
        self.list_lagu.append(Lagu(
            judul, album, penyanyi, genre, tahun,
            lokasi, durasi, waktu_saat_ini, waktu_saat_ini
        ))
    
    # Fungsi untuk menghapus objek lagu dari list_lagu
    def hapus(self, lagu):
        self.list_lagu.remove(lagu)
    
    # Fungsi mendapatkan objek lagu dari list_lagu
    def dapatkan(self, index):
        return self.list_lagu[index]
    
    # Fungsi untuk mengedit objek lagu
    def edit(self, lagu, list_properti):
        list_properti_diedit = []
        # Perulangan terhadap list properti
        # Unpack elemen list yang bertipe tuple yang berisikan (nama properti, nilai properti)
        for (nama_properti, nilai_properti) in list_properti:
            # Skip perulangan jika nilai properti kosong (user tidak ada niatan mengganti)
            if nilai_properti == "": continue
            # Tambahkan data properti yang diedit kedalam list properti diedit
            # Data nya sendiri bertipe tuple berisikan (nama properti, nilai lama, nilai baru)
            list_properti_diedit.append((
                nama_properti,
                lagu.dapatkan(nama_properti, False),
                nilai_properti
            ))
            # Ubah properti objek lagu
            setattr(lagu, nama_properti, nilai_properti)
            # Kalau lokasi file berubah, tandanya file lagu nya juga berubah, durasi nya pun juga berubah
            if nama_properti == "lokasi":
                durasi = detik_ke_string(dapatkan_durasi_lagu(nilai_properti))
                list_properti_diedit.append((
                    "durasi",
                    lagu.dapatkan("durasi", False),
                    durasi
                ))
                setattr(lagu, "durasi", durasi)
        # Jika panjang list properti diedit lebih dari 0 maka ada properti yang diubah
        # Update properti diedit (data untuk menyimpan terakhir diedit)
        if len(list_properti_diedit):
            setattr(lagu, "diedit", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        return list_properti_diedit
    
    # Mengembalikan string data yang terbuat dari list_lagu
    def ke_string(self):
        # Jika lagu kosong maka kembalikan string kosong
        if len(self.list_lagu) == 0: return ""
        # Membuat objek map dari list_lagu yang elemen nya di format dengan fungsi lambda
        list_string_data = map(
            # Format elemen list dari lagu ke string data lagu
            lambda lagu: lagu.ke_string(),
            self.list_lagu
        )
        # Gabungkan list dengan karakter "?" menjadi sekat
        return "?".join(list_string_data)
    
    # Fungsi untuk print semua lagu
    def print_semua_lagu(self, print_singkat):
        print("\nDaftar Lagu:")
        print("------------")
        # Perulangan terhadap objek enumerate yang dibuat dari list_lagu
        # Lalu unpack nilainya
        for (index, lagu) in enumerate(self.list_lagu):
            if print_singkat:
                # Print singkat cth. "1. Judul oleh Penyanyi"
                print(
                    f"{index + 1}. {lagu.dapatkan("judul", True)} "
                    f"oleh {lagu.dapatkan("penyanyi", False)}"
                )
            else:
                # cth. "1. Judul dari Album oleh Penyanyi [durasi(mm:ss)]"
                print(
                    f"{index + 1}. {lagu.dapatkan("judul", True)} "
                    f"dari {lagu.dapatkan("album", False)} "
                    f"oleh {lagu.dapatkan("penyanyi", False)} "
                    f"[{lagu.dapatkan("durasi", False)}]"
                )
    
    # Fungsi static untuk mendapatkan list_lagu dari string data
    @staticmethod
    def dari_string(string_data):
        list_lagu = []
        if string_data != "":
            # Belah string data menjadi list string data lagu
            list_string_data = string_data.split("?")
            # Buat objek map lagu dari list data lagu yang per elemen nya di format oleh fungsi lambda
            list_lagu = map(
                # Format elemen string data lagu ke objek lagu
                lambda string_data: Lagu.dari_string(string_data),
                list_string_data
            )
        # Mengembalikan list yang terbuat dari objek map
        return ManajemenLagu(list(list_lagu))
