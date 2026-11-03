# Versi 1: Alien berwarna hijau
alien_color = 'green'

if alien_color == 'green':
    print("Selamat! Pemain mendapatkan 5 poin karena alien berwarna hijau.")
elif alien_color == 'yellow':
    print("Selamat! Pemain mendapatkan 10 poin karena alien berwarna kuning.")
else:
    print("Selamat! Pemain mendapatkan 15 poin karena alien berwarna merah.")
    
# Versi 2: Alien berwarna kuning
alien_color = 'yellow'

if alien_color == 'green':
    print("Selamat! Pemain mendapatkan 5 poin karena alien berwarna hijau.")
elif alien_color == 'yellow':
    print("Selamat! Pemain mendapatkan 10 poin karena alien berwarna kuning.")
else:
    print("Selamat! Pemain mendapatkan 15 poin karena alien berwarna merah.")
    
# Versi 3: Alien berwarna merah
alien_color = 'red'

if alien_color == 'green':
    print("Selamat! Pemain mendapatkan 5 poin karena alien berwarna hijau.")
elif alien_color == 'yellow':
    print("Selamat! Pemain mendapatkan 10 poin karena alien berwarna kuning.")
else:
    print("Selamat! Pemain mendapatkan 15 poin karena alien berwarna merah.")
    
# struktur 'if-elif-else': digunakan ketika memiliki lebih dari dua kondisi yang ingin diuji secara berurutan.
# ketika salah satu kondisi bernilai benar (True), maka python akan lansgung menjalankan blok kode tersebut tanpa mengecek kondisi di bawahnya lagi.
# jadi "if-elif-else" mencegah pengecekan yang tidak perlu, karena jika diatasnya sudah benar, dia tidak akan mengecek yang bawah.
# jika yang atas salah, dia baru mengecek yang bawahnya
# misal, hijau = 5 poin, kuning = 10 poin, merah = 15 poin, maka pakai if-elif-else karena pilihannya lebih dari dua.