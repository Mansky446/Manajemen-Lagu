from modul.pemutar_lagu import dapatkan_durasi_lagu
from modul.utilitas import detik_ke_string, format_lokasi_absolute

class Lagu:
    def __init__(self, judul, album, penyanyi, genre, tahun, lokasi, diedit, ditambahkan):
        self.judul = judul
        self.album = album
        self.penyanyi = penyanyi
        self.genre = genre
        self.tahun = tahun
        self.lokasi = lokasi
        self.diedit = diedit
        self.ditambahkan = ditambahkan
        # Jika lokasi file != "" maka update durasi lagu dan lokasiabs
        # Durasi lagu dinamis sesuai panjang lagu dari file lagu itu sendiri
        if lokasi == "":
            self.lokasiabs = ""
            self.durasi = ""
            return
        
        self.lokasiabs = format_lokasi_absolute(lokasi)
        self.durasi = detik_ke_string(dapatkan_durasi_lagu(self.lokasiabs))
    
    # Fungsi untuk mendapatkan properti lagu
    def dapatkan(self, nama_properti, nilai_sebenarnya):
        nilai_properti = getattr(self, nama_properti)
        # Kalau properti ada atau nilai_sebenarnya == True, kembalikan properti tanpa nilai berbeda
        if nilai_properti != "" or nilai_sebenarnya:
            return nilai_properti
        # Jika properti kosong ("") maka kembalikan nilai yang berbeda tergantung nama propertinya
        return (
            "--:--" if nama_properti == "durasi" else
            "Tidak ada" if nama_properti == "lokasi" or nama_properti == "lokasiabs" else
            "-" if nama_properti == "tahun" or nama_properti == "genre" else
            "Tidak diketahui"
        )
    
    # Fungsi print detail properti lagu
    def print_detail(self):
        # Mengubah object lagu ke dict dan diubah lagi menjadi list yang berisi tuple nama properti dan nilai properti
        data_lagu = self.__dict__.items()
        # Perulangan untuk print nama properti: nilai properti
        for (nama_properti, _) in data_lagu:
            print(
                f"{nama_properti.capitalize()}: "
                f"{self.dapatkan(nama_properti, False)}"
            )
    
    # Mengubah objek lagu ke string
    def ke_string(self):
        # Mengubah object lagu ke dict dan diubah lagi menjadi list yang berisi tuple nilai properti
        data_lagu = self.__dict__.items()
        data_lagu = filter(
            lambda data: data[0] != "lokasiabs" and data[0] != "durasi",
            data_lagu
        )
        data_lagu = map(
            lambda data: data[1],
            data_lagu
        )
        # Membuat string dari nilai properti yang digabungkan dan disekat oleh karakter "|"
        # cth. ["judul", "album"] -> "judul|album"
        return "|".join(data_lagu)
    
    # Metode statik untuk membuat objek lagu dari string
    @staticmethod
    def dari_string(string_data):
        # Membuat list dari string, setiap bertemu karakter "|" string akan dibelah dan ditambahkan ke elemen selanjutnya
        # cth. "judul|album" -> ["judul", "album"]
        list_nilai_properti = string_data.split("|")
        # Membuat objek lagu dan meneruskan list nilai properti sebagai parameter
        return Lagu(*list_nilai_properti)
