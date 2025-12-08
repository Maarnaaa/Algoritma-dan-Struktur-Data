# Program Bubble Sort Sederhana

data = [34, 12, 5, 66, 1]

print("Data sebelum diurutkan:", data)

# Bubble Sort
for i in range(len(data)):
    for j in range(0, len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Data setelah diurutkan:", data)

#HASIL MODIFIKASI
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def bubble_sort_mahasiswa(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):

            clear()
            print("=== PROSES BUBBLE SORT DATA MAHASISWA ===\n")

            print("Membandingkan NIM:")
            print(f"{data[j]['nim']}  <-->  {data[j+1]['nim']}\n")

            print("Data sementara:")
            print("---------------------------------------------------")
            print("|    NIM    |      NAMA      |   PRODI  | FAKUKLTAS |")
            print("---------------------------------------------------")
            for m in data:
                print(f"| {m['nim']:8} | {m['nama']:^14} | {m['prodi']:^8} | {m['fakultas']:^4} |")
            print("----------------------------------------------")

            if data[j]["nim"] > data[j + 1]["nim"]:
                
                print("\n→ Terjadi pertukaran data!\n")
                data[j], data[j + 1] = data[j + 1], data[j]
            else:
                print("\n→ Tidak ditukar.\n")

            time.sleep(1)

    return data

mhs = []
jumlah = int(input("Masukkan jumlah data mahasiswa: "))

for i in range(jumlah):
    print(f"\nData ke-{i+1}")
    nama = input("Nama      : ")
    nim = input("NIM       : ")
    prodi = input("Prodi     : ")
    fakultas = input("Fakultas  : ")

    mhs.append({
        "nama": nama,
        "nim": nim,
        "prodi": prodi,
        "fakultas": fakultas
    })

print("\nMulai proses pengurutan...\n")
time.sleep(1)

hasil = bubble_sort_mahasiswa(mhs)

clear()
print("=== DATA MAHASISWA SETELAH DIURUTKAN (BERDASARKAN NIM) ===\n")
print("-------------------------------------------------------------")
print("|    NIM    |      NAMA      |        PRODI        | FAKULTAS |")
print("-------------------------------------------------------------")

for m in hasil:
    print(f"| {m['nim']:8} | {m['nama']:^14} | {m['prodi']:^18} | {m['fakultas']:^4} |")

print("-----------------------------------------------------------")