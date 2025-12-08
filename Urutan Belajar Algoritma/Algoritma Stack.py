# Program Stack Sederhana

stack = []   # membuat stack kosong

def push(data):
    stack.append(data)
    print(f"{data} berhasil ditambahkan ke stack.")

def pop():
    if len(stack) == 0:
        print("Stack kosong, tidak bisa POP.")
    else:
        data = stack.pop()
        print(f"{data} berhasil dihapus dari stack.")

def tampilkan():
    if len(stack) == 0:
        print("Stack masih kosong.")
    else:
        print("Isi stack saat ini:", stack)

# Contoh penggunaan
push("A")
push("B")
push("C")
tampilkan()

pop()
tampilkan()

#HASIL MODIFIKASI
stack = [] 

def push_mahasiswa():
    print("\n=== INPUT DATA MAHASISWA ===")
    nama = input("Nama      : ")
    nim = input("NIM       : ")
    prodi = input("Prodi     : ")
    fakultas = input("Fakultas  : ")

    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "prodi": prodi,
        "fakultas": fakultas
    }

    stack.append(mahasiswa)
    print("\nData mahasiswa berhasil ditambahkan ke stack!\n")


def pop_mahasiswa():
    if len(stack) == 0:
        print("Stack kosong, tidak ada data yang bisa dihapus.\n")
    else:
        data = stack.pop()
        print("\nData mahasiswa yang dihapus:")
        print(data, "\n")


def tampilkan_stack():
    if len(stack) == 0:
        print("Stack masih kosong.\n")
    else:
        print("\n=== ISI STACK MAHASISWA ===")
        for i, mhs in enumerate(reversed(stack), start=1):
            print(f"{i}. {mhs['nama']} - {mhs['nim']} - {mhs['prodi']} - {mhs['fakultas']}")
        print()


def menu():
    while True:
        print("===================================")
        print("        PROGRAM STACK MAHASISWA     ")
        print("===================================")
        print("1. Tambah Data Mahasiswa (PUSH)")
        print("2. Hapus Data Teratas (POP)")
        print("3. Tampilkan Semua Mahasiswa")
        print("4. Keluar")
        print("===================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            push_mahasiswa()
        elif pilihan == "2":
            pop_mahasiswa()
        elif pilihan == "3":
            tampilkan_stack()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")

menu()