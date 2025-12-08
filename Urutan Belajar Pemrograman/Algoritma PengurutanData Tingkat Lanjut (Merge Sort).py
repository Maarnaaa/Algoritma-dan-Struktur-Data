# Program Merge Sort Sederhana

def merge_sort(data):
    if len(data) > 1:
        # Bagi data menjadi dua bagian
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        # Rekursif panggil merge_sort pada masing-masing bagian
        merge_sort(left)
        merge_sort(right)

        # Gabungkan kembali
        i = j = k = 0

        # Bandingkan elemen kiri dan kanan
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        # Salin sisa elemen jika ada
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

# Contoh penggunaan
data = [33, 9, 1, 8, 27, 67, 14, 23]
print("Data sebelum diurutkan:")
print(data)

merge_sort(data)

print("\nData setelah diurutkan (Merge Sort):")
print(data)

#HASIL MODIFIKASI
def merge_sort(data, key, ascending=True):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left, key, ascending)
        merge_sort(right, key, ascending)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if ascending:
                condition = str(left[i][key]).lower() <= str(right[j][key]).lower() if isinstance(left[i][key], str) else left[i][key] <= right[j][key]
            else:
                condition = str(left[i][key]).lower() >= str(right[j][key]).lower() if isinstance(left[i][key], str) else left[i][key] >= right[j][key]

            if condition:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

n = int(input("Masukkan jumlah buku: "))
buku = []

for i in range(n):
    judul = input(f"\nMasukkan judul buku ke-{i+1}: ")
    pengarang = input(f"Masukkan pengarang buku '{judul}': ")
    while True:
        try:
            tahun = int(input(f"Masukkan tahun terbit buku '{judul}': "))
            break
        except ValueError:
            print("Harap masukkan angka untuk tahun terbit.")
    buku.append({"judul": judul, "pengarang": pengarang, "tahun": tahun})

print("\nDaftar buku sebelum diurutkan:")
print("{:<30} {:<20} {:>10}".format("Judul", "Pengarang", "Tahun"))
print("-"*62)
for b in buku:
    print("{:<30} {:<20} {:>10}".format(b['judul'], b['pengarang'], b['tahun']))

key_map = {"judul": "judul", "pengarang": "pengarang", "tahun": "tahun"}
while True:
    kriteria = input("\nUrutkan berdasarkan (judul/pengarang/tahun)? ").strip().lower()
    if kriteria in key_map:
        break
    print("Pilihan tidak valid. Masukkan 'judul', 'pengarang', atau 'tahun'.")

urutan = input("Urutkan ascending(a) atau descending(d)? ").strip().lower()
ascending = True if urutan == 'a' else False

merge_sort(buku, key_map[kriteria], ascending)

print("\nDaftar buku setelah diurutkan:")
print("{:<5} {:<30} {:<20} {:>10}".format("No", "Judul", "Pengarang", "Tahun"))
print("-"*70)
for idx, b in enumerate(buku, 1):
    print("{:<5} {:<30} {:<20} {:>10}".format(idx, b['judul'], b['pengarang'], b['tahun']))

while True:
    cari = input("\nCari buku berdasarkan judul atau pengarang (ketik 'exit' untuk berhenti): ").strip()
    if cari.lower() == "exit":
        print("Program selesai.")
        break

    hasil = [(idx+1, b) for idx, b in enumerate(buku) 
             if cari.lower() in b['judul'].lower() or cari.lower() in b['pengarang'].lower()]
    if hasil:
        print("\nHasil pencarian:")
        print("{:<5} {:<30} {:<20} {:>10}".format("No", "Judul", "Pengarang", "Tahun"))
        print("-"*70)
        for pos, b in hasil:
            print("{:<5} {:<30} {:<20} {:>10}".format(pos, b['judul'], b['pengarang'], b['tahun']))
    else:
        print("Buku tidak ditemukan.")