# 1. Meminta input dari pengguna dan mengubahnya menjadi tipe data integer (angka)
party_size = input("Berapa orang jumlah dalam kelompok makan malam Anda? ")
party_size = int(party_size)

# 2. Menggunakan struktur kondisi if-else untuk mengecek ketersediaan meja
if party_size > 8:
    print("\nMohon maaf, Anda harus menunggu meja terlebih dahulu karena kelompok Anda lebih dari 8 orang.")
else:
    print("\nSilakan masuk, meja Anda sudah siap!")