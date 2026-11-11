import json

filename = 'favorite_number.json'

try:
    # Coba memuat angka favorit dari file jika sudah ada
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    # Jika file belum ada, minta input dari pengguna
    favorite_number = input("Berapa angka favoritmu? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print("Baiklah, saya akan mengingatnya saat kamu kembali!")
else:
    # Jika file berhasil ditemukan dan dibaca
    print(f"Saya tahu angka favoritmu! Itu adalah angka {favorite_number}.")