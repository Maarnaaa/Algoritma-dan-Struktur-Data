# Daftar data
data = ["Andi", "Budi", "Sari", "Rina", "Doni"]

print("Data dalam list:")
print(data)

# Input data yang dicari
cari = input("\nMasukkan nama yang ingin dicari: ")

# Algoritma searching sederhana
ketemu = False
for i in range(len(data)):
    if data[i].lower() == cari.lower():
        ketemu = True
        posisi = i
        break

# Output hasil
if ketemu:
    print(f"\nData '{cari}' ditemukan pada indeks ke-{posisi}")
else:
    print(f"\nData '{cari}' TIDAK ditemukan dalam list")

#HASIL MODIFIKASI
import time
import os
import sys

#Warna
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
B = "\033[34m"
C = "\033[36m"
M = "\033[35m"
W = "\033[0m"

def loading(text="Loading"):
    for i in range(12):
        anim = ["-", "\\", "|", "/"][i % 4]
        print(f"{Y}{text} {anim}{W}", end="\r")
        time.sleep(0.1)
    print(" " * 30, end="\r")

def beep():
    sys.stdout.write("\a")
    sys.stdout.flush()

def show_table(data):
    print(f"\n{C}========== TABEL DATA =========={W}")
    print(f"{B}+-------+-------------------+{W}")
    print(f"{B}| Index | Data              |{W}")
    print(f"{B}+-------+-------------------+{W}")

    for idx, item in enumerate(data):
        print(f"{B}|{W}  {idx:<5}{B}|{W} {item:<18}{B}|{W}")

    print(f"{B}+-------+-------------------+{W}\n")

def linear_search(data, target):
    print(f"\n{M}=== PROSES LINEAR SEARCH ==={W}")

    for i in range(len(data)):
        print(f"{C}Pointer → Index {i} : {data[i]}{W}")
        time.sleep(0.35)

        if data[i].lower() == target.lower():
            beep()
            return i
    return -1

def binary_search(data, target):
    print(f"\n{B}=== PROSES BINARY SEARCH ==={W}")

    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        mid = (kiri + kanan) // 2
        print(f"{C}Pointer → Mid {mid} : {data[mid]}{W}")
        time.sleep(0.35)

        if data[mid].lower() == target.lower():
            beep()
            return mid
        elif target.lower() < data[mid].lower():
            kanan = mid - 1
        else:
            kiri = mid + 1

    return -1

def menu():
    data = []

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"""{Y}
=========================================
       PROGRAM SEARCHING SUPER WAH
=========================================
1. Tambah Data
2. Lihat Data (Tabel)
3. Searching (Auto: Linear/Binary)
4. Sorting Data
5. Keluar
========================================={W}""")

        p = input("Pilih menu: ")

        if p == "1":
            nama = input("\nMasukkan data baru: ")
            loading("Menambahkan")
            data.append(nama)
            print(f"{G}✔ '{nama}' berhasil ditambahkan!{W}")
            time.sleep(1)

        elif p == "2":
            if not data:
                print(f"{R}Data masih kosong!{W}")
            else:
                show_table(data)
            input("Tekan Enter untuk kembali...")

        elif p == "3":
            if not data:
                print(f"{R}Tidak bisa mencari! Data kosong.{W}")
                time.sleep(1)
                continue

            target = input("\nMasukkan data yang ingin dicari: ")
            print()
            loading("Scanning")

            if data == sorted(data):
                posisi = binary_search(data, target)
            else:
                posisi = linear_search(data, target)

            print(f"\n{Y}=== HASIL SEARCHING ==={W}")
            if posisi != -1:
                print(f"{G}✔ Data '{target}' ditemukan pada index {posisi}{W}\n")
            else:
                print(f"{R}✘ Data '{target}' tidak ditemukan.{W}\n")

            input("Tekan Enter untuk kembali...")

        elif p == "4":
            print("\nMelakukan sorting...")
            loading("Sorting")
            data.sort()
            print(f"{G}✔ Data berhasil diurutkan!{W}")
            time.sleep(1)

        elif p == "5":
            print(f"{Y}Menutup program...{W}")
            loading("Closing")
            break

        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

if __name__ == "__main__":
    menu()