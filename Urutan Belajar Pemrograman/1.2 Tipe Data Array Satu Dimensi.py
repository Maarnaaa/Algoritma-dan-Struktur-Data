# Array satu dimensi berisi angka
nilai = [80, 75, 90, 85, 70]

print("Isi array:")
print(nilai)

# Mengakses elemen array
print("\nElemen pertama:", nilai[0])
print("Elemen ketiga :", nilai[2])

# Mengubah elemen array
nilai[1] = 88
print("\nArray setelah diubah:", nilai)

# Menambahkan elemen baru
nilai.append(95)
print("Array setelah ditambah:", nilai)

#HASIL MODIFIKASI
print("========== PROGRAM ARRAY 1 DIMENSI ==========\n")
nilai = [80, 75, 90, 85, 70]

print("Data awal dalam array:")
print(nilai)

print("\n===== INFORMASI ARRAY =====")
print("Jumlah elemen :", len(nilai))
print("Nilai tertinggi:", max(nilai))
print("Nilai terendah :", min(nilai))
print("Total nilai    :", sum(nilai))
print("Rata-rata      :", sum(nilai) / len(nilai))

print("\n===== ARRAY SETELAH DIURUTKAN =====")
asc = sorted(nilai)
desc = sorted(nilai, reverse=True)

print("Urut naik (Ascending) :", asc)
print("Urut turun (Descending):", desc)

cari = 90
print("\n===== PENCARIAN NILAI =====")
if cari in nilai:
    print(f"Nilai {cari} ditemukan pada indeks ke-{nilai.index(cari)}")
else:
    print(f"Nilai {cari} tidak ada dalam array")

print("\n===== MENAMBAH NILAI BARU =====")
nilai_baru = 95
nilai.append(nilai_baru)
print(f"Nilai {nilai_baru} berhasil ditambahkan.")
print("Data sekarang:", nilai)

print("\n===== MENGHAPUS NILAI TERTENTU =====")
hapus = 75
if hapus in nilai:
    nilai.remove(hapus)
    print(f"Nilai {hapus} berhasil dihapus.")
else:
    print(f"Nilai {hapus} tidak ditemukan.")
print("Data sekarang:", nilai)

print("\n===== UPDATE NILAI =====")
index_update = 2
nilai[index_update] = 100
print(f"Nilai pada indeks {index_update} diubah menjadi 100.")
print("Data sekarang:", nilai)

for i in range(len(nilai)):
    print(f"Indeks {i} → {nilai[i]}")
