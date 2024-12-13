from os import environ
from math import ceil
from threading import Timer
from modul.utilitas import string_ke_detik

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pygame.mixer import init, Sound, music

# Fungsi untuk mendapatkan durasi lagu dari file lagu yang lokasinya ditunjuk oleh string lokasi
def dapatkan_durasi_lagu(string_lokasi):
    file_lagu = Sound(string_lokasi)
    # Mengembalikan int detik durasi lagu dari double yang dibulatkan keatas
    return ceil(file_lagu.get_length())

class PemutarLagu:
    def __init__(self):
        init()
        self.lagu_diputar = None
        self.sedang_dijeda = False
        self.pengingat = None
    
    # Mengembalikan lagu yang sedang diputar
    def dapatkan_lagu_diputar(self):
        return self.lagu_diputar
    
    # Mengembalikan status lagu yang sedang diputar apakah dijeda atau tidak
    def apakah_lagu_dijeda(self):
        return self.sedang_dijeda
    
    # FUngsi untuk putar lagu
    def mulai(self, lagu):
        music.load(lagu.lokasi)
        music.play(0, 0, 1)
        
        self.lagu_diputar = lagu
        self.sedang_dijeda = False
        # Menggunakan objek timer yang diberi delai sesuai durasi lagu (dalam int detik) untuk menjalankan fungsi berhenti
        self.pengingat = Timer(string_ke_detik(lagu.durasi), self.berhenti)
        self.pengingat.start()
    
    # Fungsi untuk berhenti memutar lagu
    def berhenti(self):
        music.stop()
        music.unload()

        self.lagu_diputar = None
        self.sedang_dijeda = False
        self.pengingat.cancel()
    
    # Fungsi untuk jeda lagu
    def jeda(self):
        music.pause()
        self.sedang_dijeda = True
    
    # Fugsi untuk mulai kembali lagu yang dijeda
    def mulai_kembali(self):
        music.unpause()
        self.sedang_dijeda = False
    
    # Fungsi untuk print data lagu yang sedang diputar
    def print_lagu_diputar(self):
        print("\nLagu yang sedang diputar:\n")
        print(f"{self.lagu_diputar.judul}, {self.lagu_diputar.dapatkan("album", False)}")
        print(f"{self.lagu_diputar.dapatkan("penyanyi", False)}")