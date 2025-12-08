# Program Array Sederhana

# Membuat array kosong
data = []

# Menambah data ke dalam array
data.append("Apel")
data.append("Jeruk")
data.append("Mangga")

# Menampilkan isi array
print("Isi array saat ini:")
print(data)

# Mengubah isi array
data[1] = "Pisang"   # Mengubah Jeruk menjadi Pisang

# Menampilkan isi setelah diubah
print("\nSetelah diubah:")
print(data)

# Menghapus data dari array
data.remove("Apel")

# Menampilkan isi terakhir
print("\nSetelah dihapus:")
print(data)

#HASIL MODIFIKASI
import os
import time

# Warna terminal
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
C = "\033[36m"
W = "\033[0m"

def loading(text="Loading"):
    for i in range(3):
        print(f"{C}{text}{'.'*(i+1)}{W}", end="\r")
        time.sleep(0.3)
    print(" " * 20, end="\r")

data = []

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"""{Y}
====================================
         PROGRAM ARRAY 
====================================
1. Tambah Data ke Array
2. Lihat Isi Array
3. Ubah Data dalam Array
4. Hapus Data dari Array
5. Hapus Semua Data
6. Keluar
===================================={W}""")

        pilihan = input(f"{C}Pilih menu: {W}")

        if pilihan == "1":
            item = input("Masukkan data baru: ")
            loading("Menambah")
            data.append(item)
            print(f"{G}✔ Data '{item}' berhasil ditambah!{W}")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            if not data:
                print(f"{R}Array masih kosong!{W}")
            else:
                print("\nIsi array saat ini:")
                for i, item in enumerate(data, start=1):
                    print(f"{C}{i}. {item}{W}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "3":
            if not data:
                print(f"{R}Tidak bisa mengubah, array kosong!{W}")
            else:
                print("\nData saat ini:")
                for i, item in enumerate(data, start=1):
                    print(f"{C}{i}. {item}{W}")

                try:
                    index = int(input("\nPilih nomor yang ingin diubah: ")) - 1
                    new = input("Masukkan data baru: ")

                    loading("Mengubah")
                    data[index] = new
                    print(f"{G}✔ Data berhasil diubah menjadi '{new}'!{W}")

                except:
                    print(f"{R}Input tidak valid!{W}")

            input("Tekan Enter untuk kembali...")

        elif pilihan == "4":
            if not data:
                print(f"{R}Tidak bisa menghapus, array kosong!{W}")
            else:
                print("\nData saat ini:")
                for i, item in enumerate(data, start=1):
                    print(f"{C}{i}. {item}{W}")

                try:
                    index = int(input("\nPilih nomor yang ingin dihapus: ")) - 1
                    removed = data.pop(index)

                    loading("Menghapus")
                    print(f"{G}✔ Data '{removed}' berhasil dihapus!{W}")
                except:
                    print(f"{R}Input tidak valid!{W}")

            input("Tekan Enter untuk kembali...")

        elif pilihan == "5":
            if not data:
                print(f"{R}Array sudah kosong!{W}")
            else:
                loading("Membersihkan")
                data.clear()
                print(f"{G}✔ Semua data berhasil dihapus!{W}")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "6":
            loading("Keluar")
            print(f"{Y}Program selesai.{W}")
            break

        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

if __name__ == "__main__":
    menu()