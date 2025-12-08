# Program Quick Sort Sederhana

def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]  # memilih elemen pertama sebagai pivot
        less = [x for x in data[1:] if x <= pivot]
        greater = [x for x in data[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Contoh penggunaan dengan data angka baru
data = [45, 7, 23, 89, 12, 34, 56, 3]
print("Data sebelum diurutkan:")
print(data)

data_sorted = quick_sort(data)

print("\nData setelah diurutkan (Quick Sort):")
print(data_sorted)


#HASIL MODIFIKASI
def quick_sort(data, key, ascending=True):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        if ascending:
            less = [x for x in data[1:] if x[key] <= pivot[key]]
            greater = [x for x in data[1:] if x[key] > pivot[key]]
        else:
            less = [x for x in data[1:] if x[key] >= pivot[key]]
            greater = [x for x in data[1:] if x[key] < pivot[key]]
        return quick_sort(less, key, ascending) + [pivot] + quick_sort(greater, key, ascending)

n = int(input("Masukkan jumlah pengunjung: "))
pengunjung = []

for i in range(n):
    nama = input(f"\nMasukkan nama pengunjung ke-{i+1}: ")
    while True:
        try:
            umur = int(input(f"Masukkan umur {nama}: "))
            break
        except ValueError:
            print("Harap masukkan angka untuk umur.")
    while True:
        try:
            tiket = int(input(f"Masukkan nomor tiket {nama}: "))
            break
        except ValueError:
            print("Harap masukkan angka untuk nomor tiket.")
    pengunjung.append({"nama": nama, "umur": umur, "tiket": tiket})

print("\nDaftar pengunjung sebelum diurutkan:")
print("{:<30} {:>5} {:>10}".format("Nama", "Umur", "Tiket"))
print("-"*50)
for p in pengunjung:
    print("{:<30} {:>5} {:>10}".format(p['nama'], p['umur'], p['tiket']))

key_map = {"nama": "nama", "umur": "umur", "tiket": "tiket"}
while True:
    kriteria = input("\nUrutkan berdasarkan (nama/umur/tiket)? ").strip().lower()
    if kriteria in key_map:
        break
    print("Pilihan tidak valid. Masukkan 'nama', 'umur', atau 'tiket'.")

urutan = input("Urutkan ascending(a) atau descending(d)? ").strip().lower()
ascending = True if urutan == 'a' else False

pengunjung_sorted = quick_sort(pengunjung, key_map[kriteria], ascending)

print("\nDaftar pengunjung setelah diurutkan:")
print("{:<5} {:<30} {:>5} {:>10}".format("No", "Nama", "Umur", "Tiket"))
print("-"*55)
for idx, p in enumerate(pengunjung_sorted, 1):
    print("{:<5} {:<30} {:>5} {:>10}".format(idx, p['nama'], p['umur'], p['tiket']))
