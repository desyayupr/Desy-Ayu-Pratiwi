# menyimpan nama dengan karakter whitespace (\t dan \n) di awal dan akhir
nama_spasi = "\t\n Albert Einstein \n\t"

# 1. print nama asli dengan whitespace
print("Nama dengan karakter whitespace")
print(nama_spasi)

# 2. menggunakan lstrip() untuk menghapus whitespace disebelah kiri (beginning)
print("\nMenggunakan lstrip(): ")
print(nama_spasi.lstrip())

# 3. menggunakan rstrip() untuk menghapus whitespace disebelah kanan (end)
print("\nMenggunakan rstrip(): ")
print(nama_spasi.rstrip())

# 4. menggunakan strip() untuk menghapus whitespace dikedua sisi (beginning and end)
print("\nMenggunakan strip(): ")
print(nama_spasi.strip())

# note:
# \t dan \n : dimana \t untuk tab (jarak kosong horizontal) dan \n untuk newline (garis baru)
# .lstrip() : menghapus spasi atau karakter kosong (whitespace) dibagian kiri (awal) string
# .rstrip(): menghapus spasi atau karakter kosong dibagian kanan (akhir) string
# strip() : menghapus spasi atau karakter kosong (whitespace) di kedua sisi (awal dan akhir) secara bersamaan
