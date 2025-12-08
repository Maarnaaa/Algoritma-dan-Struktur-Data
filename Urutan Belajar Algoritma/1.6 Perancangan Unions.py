# Perancangan Unions Sederhana

class DataSerbaguna:
    def __init__(self):
        self.active_type = None
        self.value = None

    def setInteger(self, x):
        self.active_type = "Integer"
        self.value = x

    def setFloat(self, x):
        self.active_type = "Float"
        self.value = x

    def setString(self, x):
        self.active_type = "String"
        self.value = x

    def show(self):
        print("===== DATA UNION =====")
        print("Tipe data aktif :", self.active_type)
        print("Nilai           :", self.value)
        print("======================\n")


# Program Utama
u = DataSerbaguna()

u.setInteger(10)
u.show()

u.setFloat(8.92)
u.show()

u.setString("Ini Union")
u.show()

#HASIL MODIFIKASI
import os
import time

#Warna
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
B = "\033[34m"
C = "\033[36m"
P = "\033[35m"
W = "\033[0m"

def loading(txt="Memproses"):
    for i in range(4):
        print(f"{C}{txt}{'.' * i}{W}", end="\r")
        time.sleep(0.3)
    print(" " * 30, end="\r")


class UnionWah:
    """Simulasi UNION gaya Python."""
    
    def __init__(self):
        self.active_type = None
        self.value = None

    def setInteger(self, v):
        self.active_type = "Integer"
        self.value = v
        print(f"{G}✔ Integer disimpan!{W}")
        time.sleep(0.4)

    def setFloat(self, v):
        self.active_type = "Float"
        self.value = v
        print(f"{G}✔ Float disimpan!{W}")
        time.sleep(0.4)

    def setString(self, v):
        self.active_type = "String"
        self.value = v
        print(f"{G}✔ String disimpan!{W}")
        time.sleep(0.4)

    def show(self):
        print(f"""
{Y}==============================
         DATA UNION AKTIF
=============================={W}
Tipe Data : {C}{self.active_type}{W}
Nilai     : {G}{self.value}{W}
{Y}=============================={W}
""")


def header():
    print(f"""
{P}============================================
               PROGRAM UNION 
============================================{W}
""")
def menu():
    u = UnionWah()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        header()

        print(f"""
{C}1. Simpan Integer
2. Simpan Float
3. Simpan String
4. Lihat Data Aktif
5. Reset Union
6. Keluar
{W}
""")

        pilihan = input(f"{Y}Pilih menu → {W}")

        if pilihan == "1":
            x = int(input("Masukkan angka integer: "))
            loading("Menyimpan integer")
            u.setInteger(x)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            x = float(input("Masukkan angka float: "))
            loading("Menyimpan float")
            u.setFloat(x)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":
            x = input("Masukkan teks: ")
            loading("Menyimpan string")
            u.setString(x)
            input("Tekan Enter untuk kembali...")

        elif pilihan == "4":
            loading("Mengambil data")
            if u.active_type is None:
                print(f"{R}Belum ada data dalam union!{W}")
            else:
                u.show()
            input("Tekan Enter untuk kembali...")

        elif pilihan == "5":
            loading("Mereset union")
            u = UnionWah()
            print(f"{G}✔ Union berhasil di-reset!{W}")
            time.sleep(1)

        elif pilihan == "6":
            loading("Menutup program")
            print(f"{Y}Program selesai. Sampai jumpa!{W}")
            break

        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

if __name__ == "__main__":
    menu()