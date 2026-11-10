from random import randint

# Menghasilkan angka acak antara 1 sampai 6 (seperti melempar dadu)
dadu = randint(1, 6)
print(f"Hasil lemparan dadu: {dadu}")

from random import choice

# Memilih menu makanan secara acak
menu_makanan = ["Nasi Goreng", "Sate Ayam", "Bakso", "Mie Ayam"]
pilihan = choice(menu_makanan)
print(f"Rekomendasi makan hari ini: {pilihan}")

from random import shuffle

kartu = ["AS", "King", "Queen", "Jack"]
shuffle(kartu)
print(f"Urutan kartu setelah dikocok: {kartu}")