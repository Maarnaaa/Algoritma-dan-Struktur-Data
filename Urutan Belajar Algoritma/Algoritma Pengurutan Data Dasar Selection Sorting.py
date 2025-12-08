# Program Selection Sorting Sederhana

# Data yang akan diurutkan
data = [7, 2, 9, 4, 1]

print("Data sebelum diurutkan:")
print(data)

# Selection Sort
n = len(data)

for i in range(n):
    # Anggap indeks i sebagai nilai terkecil
    min_index = i

    # Cari nilai terkecil di sisa array
    for j in range(i + 1, n):
        if data[j] < data[min_index]:
            min_index = j

    # Tukar posisi nilai terkecil dengan posisi i
    data[i], data[min_index] = data[min_index], data[i]

print("\nData setelah diurutkan:")
print(data)

#HASIL MODIFIKASI
import os
import time

#Warna
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
C = "\033[36m"
W = "\033[0m"

def loading(text="Loading"):
    for i in range(3):
        print(f"{C}{text}{'.'*(i+1)}{W}", end="\r")
        time.sleep(0.4)
    print(" " * 20, end="\r")

def tampilkan_tabel(data):
    print(f"{Y}\n==============================================================")
    print("                     DATA MAHASISWA")
    print("==============================================================")
    print(f"{C}NO  | NAMA                     | NIM        | PRODI        | FAKULTAS")
    print("-----------------------------------------------------------------------")

    for i, m in enumerate(data, start=1):
        print(f"{W}{i:<3} | {m['nama']:<24} | {m['nim']:<10} | {m['prodi']:<12} | {m['fakultas']}")

    print("==============================================================\n")

def selection_sort(data, key):
    n = len(data)
    loading(f"Mengurutkan berdasarkan {key.upper()}")

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j][key].lower() < data[min_index][key].lower():
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

def menu():
    mahasiswa = []

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"""{G}
======================================================
          PROGRAM SELECTION SORTING
======================================================
1. Tambah Data Mahasiswa
2. Lihat Data Mahasiswa
3. Sorting Berdasarkan:
      - Nama
      - NIM
      - Prodi
      - Fakultas
4. Hapus Seluruh Data
5. Keluar Program
======================================================{W}""")

        pilihan = input(f"{C}Pilih menu: {W}")

        if pilihan == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Y}=== INPUT DATA MAHASISWA ==={W}")

            nama = input("Nama     : ")
            nim = input("NIM      : ")
            prodi = input("Prodi    : ")
            fakultas = input("Fakultas : ")

            mahasiswa.append({
                "nama": nama,
                "nim": nim,
                "prodi": prodi,
                "fakultas": fakultas
            })

            loading("Menyimpan data")
            print(f"{G}✔ Data berhasil ditambahkan!{W}")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")

            if not mahasiswa:
                print(f"{R}Belum ada data mahasiswa!{W}")
            else:
                tampilkan_tabel(mahasiswa)

            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":
            if not mahasiswa:
                print(f"{R}Data kosong! Tidak bisa sorting.{W}")
                time.sleep(1)
                continue

            print(f"""{Y}
--- PILIH SORTING BERDASARKAN ---
1. Nama
2. NIM
3. Prodi
4. Fakultas
{W}""")

            pilih_sort = input("Pilih: ")

            if pilih_sort == "1":
                selection_sort(mahasiswa, "nama")
            elif pilih_sort == "2":
                selection_sort(mahasiswa, "nim")
            elif pilih_sort == "3":
                selection_sort(mahasiswa, "prodi")
            elif pilih_sort == "4":
                selection_sort(mahasiswa, "fakultas")
            else:
                print(f"{R}Pilihan tidak valid!{W}")
                time.sleep(1)
                continue

            print(f"{G}✔ Data berhasil diurutkan!{W}")
            tampilkan_tabel(mahasiswa)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "4":
            mahasiswa.clear()
            print(f"{R}Semua data sudah dihapus!{W}")
            time.sleep(1)

        elif pilihan == "5":
            print(f"{Y}Keluar dari program...{W}")
            loading("Menutup")
            break

        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

menu()