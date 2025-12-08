print("===== PROGRAM FLOATING POINT SEDERHANA =====")

# Input angka desimal dari user
angka1 = float(input("Masukkan angka desimal pertama: "))
angka2 = float(input("Masukkan angka desimal kedua: "))

print("\n===== HASIL PERHITUNGAN =====")

# Operasi menggunakan float
jumlah = angka1 + angka2
selisih = angka1 - angka2
perkalian = angka1 * angka2
pembagian = angka1 / angka2 if angka2 != 0 else "Tidak bisa membagi dengan 0"

# Menampilkan hasil
print("Angka pertama:", angka1)
print("Angka kedua  :", angka2)
print("Penjumlahan :", jumlah)
print("Pengurangan :", selisih)
print("Perkalian   :", perkalian)
print("Pembagian   :", pembagian)

# Nilai rata-rata
rata_rata = (angka1 + angka2) / 2
print("Rata-rata   :", rata_rata)

#HASIL MODIFIKASI
print("==============================================")
print("        PROGRAM FLOATING POINT KALKULATOR      ")
print("==============================================")
angka1 = float(input("Masukkan angka desimal pertama : "))
angka2 = float(input("Masukkan angka desimal kedua   : "))

jumlah = angka1 + angka2
selisih = angka1 - angka2
perkalian = angka1 * angka2
pembagian = angka1 / angka2 if angka2 != 0 else "ERROR"
rata_rata = (angka1 + angka2) / 2

def layar(label, nilai):
    nilai_str = str(nilai)
    print("┌──────────────────────────────────────┐")
    print(f"│ {label:<12}: {nilai_str:>18} │")
    print("└──────────────────────────────────────┘")

print("\n========== HASIL KALKULATOR==========\n")
layar("Penjumlahan", jumlah)
layar("Pengurangan", selisih)
layar("Perkalian", perkalian)
layar("Pembagian", pembagian)
layar("Rata-rata", rata_rata)