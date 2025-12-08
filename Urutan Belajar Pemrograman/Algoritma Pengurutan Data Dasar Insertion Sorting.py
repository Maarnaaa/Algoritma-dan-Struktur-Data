# Program Insertion Sort Sederhana

data = [5, 2, 9, 1, 7]

print("Data sebelum diurutkan:")
print(data)

# Algoritma insertion sort
for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    
    # Geser elemen yang lebih besar ke kanan
    while j >= 0 and key < data[j]:
        data[j + 1] = data[j]
        j -= 1
    
    data[j + 1] = key

print("\nData setelah diurutkan (Insertion Sort):")
print(data)

#HASIL MODIFIKASI
import os
import time

# Warna
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
C = "\033[36m"
W = "\033[0m"

def tampilkan_data(data):
    print(f"\n{Y}===== TABEL DATA BUAH & HARGA ====={W}")
    print(f"{C}{'No':<5}{'Nama Buah':<15}{'Harga (Rp)':<15}{W}")
    print("-" * 35)
    for i, (nama, harga) in enumerate(data, start=1):
        print(f"{i:<5}{nama:<15}{harga:<15}")
    print("-" * 35)

def insertion_sort(data, ascending=True):
    print(f"\n{Y}=== PROSES INSERTION SORT ==={W}")
    time.sleep(0.5)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        print(f"\n{G}Memasukkan: {key[0]} (Rp{key[1]}){W}")
        time.sleep(0.5)

        if ascending:

            while j >= 0 and key[1] < data[j][1]:
                print(f"{C}Geser {data[j][0]} ke kanan{W}")
                data[j + 1] = data[j]
                j -= 1
                time.sleep(0.4)
        else:

            while j >= 0 and key[1] > data[j][1]:
                print(f"{C}Geser {data[j][0]} ke kanan{W}")
                data[j + 1] = data[j]
                j -= 1
                time.sleep(0.4)

        data[j + 1] = key
        print(f"{G}→ Posisi baru: {key[0]}{W}")
        time.sleep(0.5)

        tampilkan_data(data)
        time.sleep(1)

    print(f"\n{G}=== DATA SELESAI DIURUTKAN ==={W}")

def main():
    data = []

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""{Y}
=====================================
        PROGRAM INSERTION SORT 
   Urutkan Buah Berdasarkan Harga
=====================================
1. Tambah Buah & Harga
2. Tampilkan Semua Data
3. Urutkan (Ascending - Murah → Mahal)
4. Urutkan (Descending - Mahal → Murah)
5. Keluar
========================================={W}""")

        pilihan = input(f"{C}Pilih menu: {W}")

        if pilihan == "1":
            nama = input("Masukkan nama buah  : ")
            harga = int(input("Masukkan harga buah : Rp "))
            data.append((nama, harga))
            print(f"{G}Data berhasil ditambahkan!{W}")
            time.sleep(1)

        elif pilihan == "2":
            if not data:
                print(f"{R}Data masih kosong! Tambahkan dulu.{W}")
            else:
                tampilkan_data(data)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":
            if not data:
                print(f"{R}Tidak bisa sorting, data kosong!{W}")
            else:
                insertion_sort(data, ascending=True)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "4":
            if not data:
                print(f"{R}Tidak bisa sorting, data kosong!{W}")
            else:
                insertion_sort(data, ascending=False)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "5":
            print(f"{G}Keluar dari program...{W}")
            time.sleep(1)
            break

        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

if __name__ == "__main__":
    main()