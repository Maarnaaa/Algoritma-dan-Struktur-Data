class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

# Membuat objek struktur
m1 = Mahasiswa("Andi", "20231001", 85)
m2 = Mahasiswa("Siti", "20231002", 90)

# Menampilkan data
print("=== Data Mahasiswa ===")
print("Nama :", m1.nama)
print("NIM  :", m1.nim)
print("Nilai:", m1.nilai)

print("\n=== Data Mahasiswa ke-2 ===")
print("Nama :", m2.nama)
print("NIM  :", m2.nim)
print("Nilai:", m2.nilai)

#HASIL MODIFIKASI
import os
import time
from datetime import datetime

R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
C = "\033[36m"
W = "\033[0m"

def loading(text="Loading"):
    for i in range(3):
        print(f"{C}{text}{'.' * (i+1)}{W}", end="\r")
        time.sleep(0.4)
    print(" " * 20, end="\r")

class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

daftar_mhs = []

def simpan_ke_file():
    with open("data_mahasiswa.txt", "w") as f:
        for m in daftar_mhs:
            f.write(f"{m.nama},{m.nim},{m.nilai}\n")

    print(f"{G}✔ Data berhasil disimpan ke file!{W}")


def load_dari_file():
    try:
        with open("data_mahasiswa.txt", "r") as f:
            daftar_mhs.clear()
            for line in f:
                nama, nim, nilai = line.strip().split(",")
                daftar_mhs.append(Mahasiswa(nama, nim, float(nilai)))
        print(f"{G}✔ Data berhasil dimuat dari file!{W}")

    except FileNotFoundError:
        print(f"{R}❌ File tidak ditemukan!{W}")


def hitung_rata_rata():
    if not daftar_mhs:
        print(f"{R}Belum ada data untuk dihitung!{W}")
        return

    total = sum(m.nilai for m in daftar_mhs)
    rata = total / len(daftar_mhs)
    print(f"\nRata-rata nilai mahasiswa adalah: {Y}{rata:.2f}{W}")


def urutkan_data():
    if not daftar_mhs:
        print(f"{R}Tidak ada data untuk diurutkan!{W}")
        return

    print("""
1. Urutkan berdasarkan Nama
2. Urutkan berdasarkan Nilai
""")

    pilih = input("Pilih jenis pengurutan: ")

    if pilih == "1":
        daftar_mhs.sort(key=lambda x: x.nama)
        print(f"{G}✔ Data berhasil diurutkan berdasarkan NAMA{W}")
    elif pilih == "2":
        daftar_mhs.sort(key=lambda x: x.nilai, reverse=True)
        print(f"{G}✔ Data berhasil diurutkan berdasarkan NILAI{W}")
    else:
        print(f"{R}Pilihan tidak valid!{W}")

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"""{Y}
=========================================
      PROGRAM STRUKTUR MAHASISWA 
=========================================
1. Tambah Mahasiswa
2. Lihat Semua Data
3. Cari Mahasiswa
4. Edit Data Mahasiswa
5. Hapus Data
6. Waktu Sistem
7. Hitung Rata-rata Nilai
8. Urutkan Data Mahasiswa
9. Simpan Ke File
10. Load Data dari File
11. Keluar
========================================={W}""")

        pilih = input(f"{C}Pilih menu: {W}")

        if pilih == "1":
            nama = input("Masukkan nama: ")
            nim = input("Masukkan NIM: ")
            nilai = float(input("Masukkan nilai: "))
            loading("Menyimpan data")
            daftar_mhs.append(Mahasiswa(nama, nim, nilai))
            print(f"{G}✔ Data mahasiswa berhasil ditambahkan!{W}")
            input("Tekan Enter...")

        elif pilih == "2":
            if not daftar_mhs:
                print(f"{R}Belum ada data mahasiswa!{W}")
            else:
                print(f"\n{C}=== DAFTAR MAHASISWA ==={W}")
                for i, m in enumerate(daftar_mhs, start=1):
                    print(f"{i}. {Y}{m.nama}{W} | NIM: {m.nim} | Nilai: {G}{m.nilai}{W}")
            input("Tekan Enter...")

        elif pilih == "3":
            cari = input("Masukkan NIM yang dicari: ")
            for m in daftar_mhs:
                if m.nim == cari:
                    print(f"{G}Data ditemukan!{W}")
                    print(f"Nama  : {m.nama}")
                    print(f"NIM   : {m.nim}")
                    print(f"Nilai : {m.nilai}")
                    break
            else:
                print(f"{R}❌ Data tidak ditemukan.{W}")
            input("Tekan Enter...")

        elif pilih == "4":
            nim_edit = input("Masukkan NIM: ")
            for m in daftar_mhs:
                if m.nim == nim_edit:
                    print("\n1. Edit Nama\n2. Edit Nilai")
                    opsi = input("Pilih opsi: ")
                    if opsi == "1":
                        m.nama = input("Nama baru: ")
                    elif opsi == "2":
                        m.nilai = float(input("Nilai baru: "))
                    print(f"{G}✔ Data diperbarui!{W}")
                    break
            else:
                print(f"{R}❌ NIM tidak ditemukan.{W}")
            input("Tekan Enter...")

        elif pilih == "5":
            nim_del = input("Masukkan NIM yang dihapus: ")
            for i, m in enumerate(daftar_mhs):
                if m.nim == nim_del:
                    del daftar_mhs[i]
                    print(f"{G}✔ Data dihapus!{W}")
                    break
            else:
                print(f"{R}❌ NIM tidak ditemukan.{W}")
            input("Tekan Enter...")

        elif pilih == "6":
            print(f"\nWaktu sistem: {G}{datetime.now()}{W}")
            input("Tekan Enter...")

        elif pilih == "7":
            hitung_rata_rata()
            input("Tekan Enter...")

        elif pilih == "8":
            urutkan_data()
            input("Tekan Enter...")

        elif pilih == "9":
            simpan_ke_file()
            input("Tekan Enter...")

        elif pilih == "10":
            load_dari_file()
            input("Tekan Enter...")

        elif pilih == "11":
            print(f"{Y}Keluar dari program...{W}")
            loading("Menutup")
            break

        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

if __name__ == "__main__":
    menu()