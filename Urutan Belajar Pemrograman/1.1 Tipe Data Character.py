#Python tidak punya tipe data char, kita bisa memakai string 1 huruf sebagai karakter.
ch = input("Masukkan 1 karakter: ")
#Validasi: harus 1 huruf
if len(ch) != 1:
    print("Error: Masukkan hanya 1 karakter saja!")
    exit()

print("\nKarakter yang dimasukkan:", ch)

#Mengecek huruf / angka / simbol
if ch.isalpha():
    print("Ini adalah huruf.")

    #Mengecek apakah vokal atau konsonan
    if ch.lower() in ['a', 'i', 'u', 'e', 'o']:
        print("Huruf vokal.")
    else:
        print("Huruf konsonan.")

    #Ubah huruf
    print("Uppercase:", ch.upper())
    print("Lowercase:", ch.lower())
    
elif ch.isdigit():
    print("Ini angka, bukan huruf.")
else:
    print("Ini simbol, bukan huruf atau angka.")

#HASIL MODIFIKASI
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
prodi = input("Masukkan Prodi: ")
fakultas = input("Masukkan Fakultas: ")
universitas = input("Masukkan Universitas: ")
umur = input("Masukkan Umur: ")
ttl = input("Masukkan Tempat, Tanggal Lahir: ")

print("\n===== HASIL ANALISIS KARAKTER =====\n")

def analisis_karakter(label, data):
    print(f"\n{label}: {data}")
    print(f"Jumlah karakter: {len(data)}")
    print("Detail karakter:")
    
    for i, ch in enumerate(data):
        if ch.isalpha():
            jenis = "Huruf"
        elif ch.isdigit():
            jenis = "Angka"
        elif ch.isspace():
            jenis = "Spasi"
        else:
            jenis = "Simbol"
        
        print(f"  Karakter {i+1} = '{ch}'  --> {jenis}")

analisis_karakter("Nama", nama)
analisis_karakter("NIM", nim)
analisis_karakter("Prodi", prodi)
analisis_karakter("Fakultas", fakultas)
analisis_karakter("Universitas", universitas)
analisis_karakter("Umur", umur)
analisis_karakter("Tempat/Tanggal Lahir", ttl)