class Contoh:
    # Variabel statis (milik class, bukan milik object)
    hitung = 0

    def __init__(self):
        # setiap object dibuat, variabel statis bertambah
        Contoh.hitung += 1

# Membuat objek
a = Contoh()
b = Contoh()
c = Contoh()

print("Jumlah object dibuat =", Contoh.hitung)

#HASIL MODIFIKASI
import os
import time
from datetime import datetime

def loading(text="Loading"):
    for i in range(3):
        print(f"{text}{'.' * (i+1)}", end="\r")
        time.sleep(0.4)
    print(" " * 20, end="\r")


class Karakter:
    # Variabel statis
    jumlah_dibuat = 0
    daftar_nama = []

    def __init__(self, nama):
        self.nama = nama
        Karakter.jumlah_dibuat += 1
        Karakter.daftar_nama.append(nama)

        print(f"Karakter '{nama}' berhasil dibuat!")
        time.sleep(0.5)


def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("""
=========================================
       PROGRAM VARIABEL STATIS
=========================================
1. Tambah Karakter
2. Lihat Total Karakter
3. Lihat Semua Nama Karakter
4. Waktu Sistem
5. Keluar
=========================================
""")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama karakter: ")
            loading("Membuat karakter")
            Karakter(nama)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            print(f"\nTotal karakter dibuat: {Karakter.jumlah_dibuat}")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":
            if not Karakter.daftar_nama:
                print("Belum ada karakter dibuat!")
            else:
                print("\nDaftar karakter:")
                for i, nama in enumerate(Karakter.daftar_nama, start=1):
                    print(f"{i}. {nama}")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "4":
            print(f"\nWaktu sistem: {datetime.now()}")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "5":
            print("Keluar dari program...")
            loading("Menutup")
            break

        else:
            print("Pilihan tidak valid!")
            time.sleep(1)


if __name__ == "__main__":
    menu()
