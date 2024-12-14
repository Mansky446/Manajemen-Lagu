from os import system
from modul.penyimpanan import Penyimpanan
from modul.manajemen_lagu import ManajemenLagu
from modul.pemutar_lagu import PemutarLagu
from modul.manajemen_tampilan import ManajemenTampilan

# Awal masuk program
if __name__ == "__main__":
    # penyimpanan = Penyimpanan("data/data.txt")
    penyimpanan = Penyimpanan("../sample/data/data.txt")
    pemutar_lagu = PemutarLagu()
    manajemen_lagu = ManajemenLagu.dari_string(penyimpanan.muat())
    manajemen_tampilan = ManajemenTampilan(manajemen_lagu, pemutar_lagu)
    
    while not manajemen_tampilan.apakah_keluar():
        system("cls")
        manajemen_tampilan.tampilkan()
        input("\nTekan enter untuk melanjutkan ")
    
    if pemutar_lagu.dapatkan_lagu_diputar() is not None:
        pemutar_lagu.berhenti()
    
    penyimpanan.simpan(manajemen_lagu.ke_string())
