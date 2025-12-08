a = 10
b = 5

jumlah = a + b
selisih = a - b
kali = a * b
bagi = a // b   # pembagian integer
modulus = a % b # sisa bagi

print("Jumlah:", jumlah)
print("Selisih:", selisih)
print("Perkalian:", kali)
print("Pembagian integer:", bagi)
print("Sisa bagi:", modulus)

#HASIL MODIFIKASI
print("=====PROGRAM OPERASI INTEGER=====")

a = int(input("Masukkan angka pertama (a): "))
b = int(input("Masukkan angka kedua (b): "))

print("\n===== HASIL PERHITUNGAN =====")

jumlah = a + b
selisih = a - b
kali = a * b
bagi = a // b if b != 0 else "Error (pembagian nol)"
modulus = a % b if b != 0 else "Error (modulus nol)"

pangkat = a ** b
maksimum = max(a, b)
minimum = min(a, b)

habis_dibagi = (a % b == 0) if b != 0 else False

print(f"Jumlah (a + b) = {jumlah}")
print(f"Selisih (a - b) = {selisih}")
print(f"Perkalian (a * b) = {kali}")
print(f"Pembagian integer (a // b) = {bagi}")
print(f"Sisa bagi (a % b) = {modulus}")
print(f"Pangkat (a ** b) = {pangkat}")
print(f"Angka terbesar = {maksimum}")
print(f"Angka terkecil = {minimum}")

if b == 0:
    print("Tidak dapat mengecek habis dibagi (b = 0).")
else:
    if habis_dibagi:
        print(f"{a} HABIS DIBAGI {b}")
    else:
        print(f"{a} TIDAK HABIS DIBAGI {b}")