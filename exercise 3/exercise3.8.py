# 1. list tempat yang ingin dikunjungi (tidak berurutan secara alfabetis)
tempat = ["Jepang", "Swiss", "Kanada", "Korea", "Jerman"]

# 2. print list dalam urutan aslinya (raw python list)
print("Urutan asli")
print(tempat)

# 3. gunakan sorted() untuk mencetak list dalam urutan alfabet tanpa mengubah list asli
print("\nUrutan dengan sorted() (alfabet): ")
print(sorted(tempat))

# 4. tunjukkan bahwa list masih dalam urutan aslinya
print("\nList masih dalam urutan asli: ")
print(tempat)

# 5. unakan sorted() dengan reverse=True untuk mencetak dalam urutan alfabet terbalik tanpa mengubah list asli
print("\nUrutan dengan sorted(reverse=True) (alfabet terbalik): ")
print(sorted(tempat, reverse=True))

# 6. tunjukkan lagi bahwa list masih dalam urutan aslinya
print("\nList masih dalam urutan asli:")

# 7. gunakan reverse() untuk mengubah urutan list asli secara permanen
tempat.reverse()
print("\nList setelah dibalik dengan reverse():")
print(tempat)

# 8. gunakan reverse() lagi untuk mengembalikannya ke urutan asli
tempat.reverse()
print("\nList dikembalikan ke urutan asli")
print(tempat)

# 9. gunakan sort() untuk mengubah list sehingga tersimpan dalam urutan alfabet secaravpermanen
tempat.sort()
print("\nList diurutkan secara permanen (alfabet):")

# 10. gunakan sort(reverse=True) untuk mengubah list dalam urutan alfabet terbalik secara permanen
tempat.sort(reverse=True)
print("\nList diurutkan secara permanen (alfabet terbalik):")
print(tempat)

# noted:
# 1. sorted(): menampilkan isi list secara berurutan (alfabet) tanpa mengubah susunan asli dalam variabel
# 2. sorted(..., reverse=True): menampilkan isi dalam urutan abjad terbalik (z-A) untuk sementara waktu tanpa mengubah list asli
# 3. .reverse(): membalikkan urutan elemen list saat ini secara permanen (urutan kembali seperti semula)
# 4. .sort(): mengubah dan merapikan susunan elemen didalam list secara permanen berdasarkan urutan abjad
# 5. .sort(reverse=True): mengubah dan menyimpan susunan elemen didalam list secara permanen dengan urutan abjad terbalik (Z-A)