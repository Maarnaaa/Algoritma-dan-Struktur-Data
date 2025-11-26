#PERBEDAANN TUPLE DENGAN LIST

#Tuple dan list adalah tipe data Python yang dapat menyimpan beberapa nilai dalam satu variabel.
#List bersifat mutable, artinya nilai di dalamnya bisa diubah, ditambah, atau dihapus.
#Tuple bersifat immutable, artinya nilai di dalamnya tidak bisa diubah setelah dibuat.
#Menggunakan tanda kurung [ ] sebagai penulisan elemennya.
#Menggunakan tanda kurung ( ) sebagai penulisan elemennya.
#List cocok digunakan untuk data yang akan sering berubah sewaktu program berjalan.
#Tuple cocok digunakan untuk data yang bersifat tetap atau tidak boleh berubah.
#Tuple memiliki kinerja lebih cepat dan memori lebih efisien dibandingkan list.

#CONTOH TUPLE
data_mahasiswa = ("Marna", 19, "Sistem Informasi")
# Menampilkan semua isi tuple
print("Data Mahasiswa:", data_mahasiswa)
# Mengakses elemen tuple
print("Nama:", data_mahasiswa[0])
print("Umur:", data_mahasiswa[1])
print("Program Studi:", data_mahasiswa[2])
#Mencoba mengubah isi tuple (akan error karena tuple immutable)
#data_mahasiswa[1] = 20  # Jika dijalankan akan menghasilkan error
# Menghitung jumlah elemen dalam tuple
print("Jumlah elemen:", len(data_mahasiswa))

#CONTOH LIST
data_mahasiswa = ["Marna", 19, "Sistem Informasi"]
# Menampilkan semua isi list
print("Data Mahasiswa:", data_mahasiswa)
# Mengakses elemen list
print("Nama:", data_mahasiswa[0])
print("Umur:", data_mahasiswa[1])
print("Program Studi:", data_mahasiswa[2])
# Mengubah isi list (list bisa diubah)
data_mahasiswa[1] = 20  # Mengubah umur menjadi 20
# Menampilkan list setelah diubah
print("Data Mahasiswa setelah diubah:", data_mahasiswa)
# Menghitung jumlah elemen dalam list
print("Jumlah elemen:", len(data_mahasiswa))