# Contoh array 3 dimensi sederhana
array3D = [
    [   # Dimensi ke-1 (index 0)
        [1, 2, 3],      # Baris 1
        [4, 5, 6]       # Baris 2
    ],
    [   # Dimensi ke-2 (index 1)
        [7, 8, 9],      # Baris 1
        [10, 11, 12]    # Baris 2
    ]
]

print("===== ARRAY 3 DIMENSI =====")
print(array3D)

# Mengakses elemen tertentu
print("\nContoh akses beberapa elemen:")
print("Elemen [0][0][0] =", array3D[0][0][0])  # 1
print("Elemen [0][1][2] =", array3D[0][1][2])  # 6
print("Elemen [1][0][1] =", array3D[1][0][1])  # 8
print("Elemen [1][1][2] =", array3D[1][1][2])  # 12

# Menampilkan seluruh elemen 3D dengan loop
print("\n===== TAMPIL ELEMEN 3D =====")
for i in range(len(array3D)):
    print(f"Dimensi ke-{i}:")
    for j in range(len(array3D[i])):
        for k in range(len(array3D[i][j])):
            print(f"  array3D[{i}][{j}][{k}] = {array3D[i][j][k]}")
    print()

#HASIL MODIFIKASI
import random

print("===== PROGRAM ARRAY 3 DIMENSI =====")

x = int(input("Masukkan jumlah dimensi (depth): "))
y = int(input("Masukkan jumlah baris   : "))
z = int(input("Masukkan jumlah kolom   : "))

print("""
Pilih metode mengisi array:
1. Input manual
2. Isi otomatis (random)
""")
pilih = input("Pilihan: ")

array3D = []

if pilih == "1":
    print("\n=== INPUT MANUAL ===")
    for i in range(x):
        dim = []
        print(f"\nMengisi dimensi ke-{i}:")
        for j in range(y):
            baris = []
            for k in range(z):
                val = float(input(f"Elemen [{i}][{j}][{k}]: "))
                baris.append(val)
            dim.append(baris)
        array3D.append(dim)

elif pilih == "2":
    print("\n=== RANDOM OTOMATIS (1–50) ===")
    for i in range(x):
        dim = []
        for j in range(y):
            baris = [random.randint(1, 50) for _ in range(z)]
            dim.append(baris)
        array3D.append(dim)

else:
    print("Pilihan tidak valid!")

def tampil3D(arr):
    for i in range(len(arr)):
        print(f"\nDimensi ke-{i}:")
        for baris in arr[i]:
            print(baris)
    print()

# ---- MENU OPERASI ----
while True:
    print("""
===== MENU OPERASI ARRAY 3 DIMENSI =====
1. Tampilkan seluruh array 3D
2. Cari nilai terbesar & terkecil + posisinya
3. Hitung rata-rata seluruh elemen
4. Total per dimensi (depth)
5. Total per baris & kolom
6. Ubah array 3D menjadi array 1D (flatten)
7. Keluar
""")

    menu = input("Pilih (1–7): ")
 
    if menu == "1":
        print("\n=== ARRAY 3 DIMENSI ===")
        tampil3D(array3D)

    elif menu == "2":
        besar = -999999
        kecil = 999999
        pos_besar = pos_kecil = (0,0,0)

        for i in range(x):
            for j in range(y):
                for k in range(z):
                    val = array3D[i][j][k]
                    if val > besar:
                        besar = val
                        pos_besar = (i, j, k)
                    if val < kecil:
                        kecil = val
                        pos_kecil = (i, j, k)
        
        print(f"\nNilai terbesar : {besar} pada posisi {pos_besar}")
        print(f"Nilai terkecil : {kecil} pada posisi {pos_kecil}")

    elif menu == "3":
        total = 0
        count = x * y * z

        for i in range(x):
            for j in range(y):
                for k in range(z):
                    total += array3D[i][j][k]

        print(f"\nRata-rata seluruh elemen = {total / count}")

    elif menu == "4":
        print("\n=== TOTAL PER DIMENSI ===")
        for i in range(x):
            tot = sum(sum(baris) for baris in array3D[i])
            print(f"Dimensi ke-{i} → Total = {tot}")

    elif menu == "5":
        print("\n=== TOTAL BARIS & KOLOM UNTUK SETIAP DIMENSI ===")
        for i in range(x):
            print(f"\nDimensi ke-{i}:")
            # total baris
            for j in range(y):
                print(f"  Total Baris {j}  = {sum(array3D[i][j])}")
            
            # total kolom
            for k in range(z):
                total_kolom = sum(array3D[i][j][k] for j in range(y))
                print(f"  Total Kolom {k} = {total_kolom}")

    elif menu == "6":
        flatten = []
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    flatten.append(array3D[i][j][k])

        print("\n=== ARRAY 1 DIMENSI ===")
        print(flatten)

    elif menu == "7":
        print("Program selesai...")
        break

    else:
        print("Menu tidak valid!")
