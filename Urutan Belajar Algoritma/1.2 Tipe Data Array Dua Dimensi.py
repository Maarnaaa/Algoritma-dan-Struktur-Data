baris = 2
kolom = 3

data = []

for i in range(baris):
    row = []
    for j in range(kolom):
        nilai = int(input(f"Masukkan nilai [{i}][{j}]: "))
        row.append(nilai)
    data.append(row)

print("Hasil Array 2 Dimensi:")
for r in data:
    print(r)

#HASIL MODIFIKASI
print("===== PROGRAM MATRIKS 2 DIMENSI =====")

def tampil_matriks(M):
    for baris in M:
        print("|", end=" ")
        for angka in baris:
            print(f"{angka:7}", end=" ")
        print("|")
    print()


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def identitas(n):
    I = []
    for i in range(n):
        baris = []
        for j in range(n):
            baris.append(1 if i == j else 0)
        I.append(baris)
    return I

def determinan(M):
    # Untuk matriks 2x2
    if len(M) == 2 and len(M[0]) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]

    # Untuk matriks 3x3
    if len(M) == 3 and len(M[0]) == 3:
        a,b,c = M[0]
        d,e,f = M[1]
        g,h,i = M[2]
        return (a*(e*i - f*h)) - (b*(d*i - f*g)) + (c*(d*h - e*g))
    
    return "Hanya mendukung 2x2 dan 3x3"

baris = int(input("Masukkan jumlah baris matriks: "))
kolom = int(input("Masukkan jumlah kolom matriks: "))

print("\nMasukkan elemen matriks:")
M = []
for i in range(baris):
    row = []
    for j in range(kolom):
        val = float(input(f"Elemen [{i+1},{j+1}]: "))
        row.append(val)
    M.append(row)

print("\n===== MATRICS ANDA =====")
tampil_matriks(M)

while True:
    print("""
===== MENU OPERASI MATRIKS =====
1. Transpose
2. Mekanisme Determinan (2x2 & 3x3)
3. Membuat Matriks Identitas
4. Penjumlahan Dua Matriks
5. Perkalian Dua Matriks
6. Keluar
    """)

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        print("\n=== HASIL TRANSPOSE ===")
        T = transpose(M)
        tampil_matriks(T)

    elif pilih == "2":
        print("\n=== DETERMINAN ===")
        print("Determinannya =", determinan(M))

    elif pilih == "3":
        if baris != kolom:
            print("⚠ Matriks harus persegi!")
        else:
            print("\n=== MATRIKS IDENTITAS ===")
            I = identitas(baris)
            tampil_matriks(I)

    elif pilih == "4":
        print("Masukkan matriks kedua:")
        M2 = []
        for i in range(baris):
            row = []
            for j in range(kolom):
                val = float(input(f"Elemen ke-2 [{i+1},{j+1}]: "))
                row.append(val)
            M2.append(row)

        print("\n=== HASIL PENJUMLAHAN ===")
        hasil = [[M[i][j] + M2[i][j] for j in range(kolom)] for i in range(baris)]
        tampil_matriks(hasil)

    elif pilih == "5":
        print("Untuk perkalian, masukkan matriks dengan ukuran kolom cocok.")

        kolom2 = int(input("Masukkan jumlah kolom matriks kedua: "))
        M2 = []

        print("Masukkan elemen matriks kedua:")
        for i in range(kolom):
            row = []
            for j in range(kolom2):
                val = float(input(f"Elemen [{i+1},{j+1}]: "))
                row.append(val)
            M2.append(row)

        print("\n=== HASIL PERKALIAN ===")
        hasil = [[sum(M[i][k] * M2[k][j] for k in range(kolom)) for j in range(kolom2)] for i in range(baris)]
        tampil_matriks(hasil)

    elif pilih == "6":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid!")