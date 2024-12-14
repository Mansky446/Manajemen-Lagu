from modul.utilitas import apakah_file_ada, format_lokasi_absolute

class Penyimpanan:
    def __init__(self, lokasi):
        lokasi = format_lokasi_absolute(lokasi)
        # Cek, bila file tidak ada, buat file baru
        if not apakah_file_ada(lokasi):
            file_penyimpanan = open(lokasi, "w")
            file_penyimpanan.write("")
            file_penyimpanan.close()
        
        self.lokasi_file = lokasi
    
    # Baca data dari file
    def muat(self):
        file_penyimpanan = open(self.lokasi_file, "r")
        string_data = file_penyimpanan.read()
        file_penyimpanan.close()

        return string_data.strip()
    
    # Tulis data ke file
    def simpan(self, string_data):
        file_penyimpanan = open(self.lokasi_file, "w")
        file_penyimpanan.write(string_data.strip())
        file_penyimpanan.close()
