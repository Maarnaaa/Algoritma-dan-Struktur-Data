# Variabel dinamis sederhana

nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))

print("\n--- DATA ANDA ---")
print("Nama:", nama)
print("Umur:", umur)

# Variabel berubah (dinamis)
print("\nUmur Anda bertambah 1 tahun...")
umur = umur + 1

print("Umur baru:", umur)

#HASIL MODIFIKASI
import os
import time
import sys

#Warna
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
W = "\033[97m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def loading(text="Loading", speed=0.2):
    for i in range(4):
        print(f"{C}{text}{'.' * i}{RESET}", end="\r")
        time.sleep(speed)
    print(" " * 30, end="\r")


def typing(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


data = {
    "nama": None,
    "umur": None,
    "level": 1  
}


def input_data():
    clear()
    typing(G + "=== INPUT DATA DINAMIS ===" + RESET)
    data["nama"] = input(C + "Masukkan nama: " + RESET)
    data["umur"] = int(input(C + "Masukkan umur: " + RESET))
    loading("Menyimpan data")
    typing(G + "Data berhasil disimpan!\n" + RESET)
    time.sleep(1)


def tampilkan_data():
    clear()
    typing(Y + "=== DATA SEKARANG ===" + RESET)
    if data["nama"] is None:
        print(R + "Belum ada data disimpan!" + RESET)
    else:
        print(f"{C}Nama : {W}{data['nama']}")
        print(f"{C}Umur : {W}{data['umur']}")
        print(f"{C}Level: {W}{data['level']}")
    print()
    input("Tekan Enter untuk kembali...")


def tambah_umur():
    clear()
    typing(Y + "Menambahkan umur..." + RESET)
    loading("Memproses")
    if data["umur"] is None:
        typing(R + "Belum ada data! Isi data terlebih dahulu." + RESET)
    else:
        data["umur"] += 1
        typing(G + f"Umur baru: {data['umur']}" + RESET)
    input("Tekan Enter untuk kembali...")


def naik_level():
    clear()
    typing(B + "LEVEL UP SYSTEM" + RESET)
    loading("Naik level")
    if data["nama"] is None:
        typing(R + "Data belum ada! Tidak bisa naik level." + RESET)
    else:
        data["level"] += 1
        typing(G + f"Selamat! Level Anda naik menjadi {data['level']} 🎉" + RESET)
    input("Tekan Enter untuk kembali...")


def menu():
    while True:
        clear()
        print(Y + "=" * 50 + RESET)
        print(G + "      PROGRAM VARIABEL DINAMIS    " + RESET)
        print(Y + "=" * 50 + RESET)

        print(f"""{C}
1. Input / Update Data
2. Tampilkan Data
3. Tambah Umur (Dinamis)
4. Naik Level (Dinamis)
5. Keluar
{RESET}""")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            input_data()
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            tambah_umur()
        elif pilih == "4":
            naik_level()
        elif pilih == "5":
            typing(Y + "Keluar dari program..." + RESET)
            loading("Menutup program")
            break
        else:
            print(R + "Pilihan tidak valid!" + RESET)
            time.sleep(1)

menu()