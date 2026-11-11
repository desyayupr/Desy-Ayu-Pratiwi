print("--- Program Penjumlahan Dua Angka ---")

try:
    # Meminta input angka pertama dan mengubahnya ke tipe integer
    first_number = input("Masukkan angka pertama: ")
    num1 = int(first_number)
    
    # Meminta input angka kedua dan mengubahnya ke tipe integer
    second_number = input("Masukkan angka kedua: ")
    num2 = int(second_number)

except ValueError:
    # Menangkap error jika input bukan angka dan menampilkan pesan ramah
    print("Maaf, masukan yang Anda berikan bukan berupa angka yang valid.")

else:
    # Jika tidak ada error, lakukan penjumlahan dan cetak hasilnya[cite: 13]
    result = num1 + num2
    print(f"Hasil penjumlahan dari {num1} + {num2} adalah: {result}")