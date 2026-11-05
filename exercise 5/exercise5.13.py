# pada exercise ini berisi tentang refleksi keterampilan pemrograman yang telah dikuasai.
# contoh: tebak angka (guessing game)

import random

# Komputer memilih angka acak dari 1 sampai 10
angka_rahasia = random.randint(1, 10) # randint adalah singkatan dari random integer

print("=== SELAMAT DATANG DI GAME TEBAK ANGKA! ===")
print("Saya telah memilih angka antara 1 sampai 10. Coba tebak!")

# Pemain memasukkan tebakan (kita gunakan fungsi int() karena input dari pengguna berupa string)
tebakan = int(input("Masukkan angka tebakan Anda: "))

# Menggunakan struktur if-elif-else untuk memeriksa tebakan pemain
if tebakan == angka_rahasia:
    print(f"Luar biasa! Tebakan Anda benar, angkanya adalah {angka_rahasia}.")
elif tebakan > angka_rahasia:
    print(f"Tebakan Anda terlalu tinggi! Angka rahasianya adalah {angka_rahasia}.")
else:
    print(f"Tebakan Anda terlalu rendah! Angka rahasianya adalah {angka_rahasia}.")
    
# import random, dia sudah bawaan dari python
# import random & random.rendint(1, 10): berfungsi meminta python menghasilkan angka acak bulat dari rentang 1-10