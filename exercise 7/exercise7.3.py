# 1. Meminta input angka dari pengguna dan mengubahnya menjadi integer
number = input("Masukkan sebuah angka: ")
number = int(number)

# 2. Mengecek apakah angka tersebut kelipatan 10 menggunakan operator modulo (%)
# Jika sisa pembagian dengan 10 adalah 0, maka angka tersebut adalah kelipatan 10
if number % 10 == 0:
    print(f"\nAngka {number} adalah kelipatan 10.")
else:
    print(f"\nAngka {number} bukan merupakan kelipatan 10.")
    
# operator modulo (%) berfungsi untuk mencari sisa hasil bagi dari suatu pembagian
