# Program Shell Sort Sederhana

# Data yang akan diurutkan
data = [23, 12, 1, 8, 34, 54, 2, 3]

print("Data sebelum diurutkan:")
print(data)

# Algoritma Shell Sort
n = len(data)
gap = n // 2   # Jarak awal (gap)

while gap > 0:
    # Lakukan insertion sort dengan gap tertentu
    for i in range(gap, n):
        temp = data[i]
        j = i

        # Geser elemen hingga posisi yang benar ditemukan
        while j >= gap and data[j - gap] > temp:
            data[j] = data[j - gap]
            j -= gap

        data[j] = temp

    # Perkecil gap menjadi setengahnya
    gap //= 2

print("\nData setelah diurutkan (Shell Sort):")
print(data)


#HASIL MODIFIKASI
n = int(input("Masukkan jumlah barang: "))

barang = []

for i in range(n):
    nama = input(f"Masukkan nama barang ke-{i+1}: ")
    while True:
        try:
            harga = float(input(f"Masukkan harga {nama}: "))
            break
        except ValueError:
            print("Harap masukkan angka untuk harga.")
    barang.append({"nama": nama, "harga": harga})

print("\nDaftar barang sebelum diurutkan:")
print("{:<20} {:>10}".format("Nama Barang", "Harga"))
print("-"*32)
for b in barang:
    print("{:<20} {:>10.2f}".format(b['nama'], b['harga']))

kriteria = input("\nUrutkan berdasarkan (nama/harga)? ").strip().lower()
urutan = input("Urutkan ascending(a) atau descending(d)? ").strip().lower()

gap = n // 2
while gap > 0:
    for i in range(gap, n):
        temp = barang[i]
        j = i
        if kriteria == "nama":
            while j >= gap and ((barang[j - gap]['nama'].lower() > temp['nama'].lower() and urutan == 'a') or 
                                (barang[j - gap]['nama'].lower() < temp['nama'].lower() and urutan == 'd')):
                barang[j] = barang[j - gap]
                j -= gap
        elif kriteria == "harga":
            while j >= gap and ((barang[j - gap]['harga'] > temp['harga'] and urutan == 'a') or 
                                (barang[j - gap]['harga'] < temp['harga'] and urutan == 'd')):
                barang[j] = barang[j - gap]
                j -= gap
        barang[j] = temp
    gap //= 2

print("\nDaftar barang setelah diurutkan:")
print("{:<20} {:>10}".format("Nama Barang", "Harga"))
print("-"*32)
for idx, b in enumerate(barang, 1):
    print("{:<2} {:<20} {:>10.2f}".format(idx, b['nama'], b['harga']))

while True:
    cari = input("\nCari barang (ketik 'exit' untuk berhenti): ").strip()
    if cari.lower() == "exit":
        print("Program selesai.")
        break

    hasil = [ (idx+1, b) for idx, b in enumerate(barang) if cari.lower() in b['nama'].lower() ]
    if hasil:
        print("\nHasil pencarian:")
        print("{:<5} {:<20} {:>10}".format("No", "Nama Barang", "Harga"))
        print("-"*36)
        for pos, b in hasil:
            print("{:<5} {:<20} {:>10.2f}".format(pos, b['nama'], b['harga']))
    else:
        print("Barang tidak ditemukan.")