import json

# Meminta input angka favorit dari pengguna
favorite_number = input("Berapa angka favorit Anda? ")

# Nama file tempat penyimpanan data JSON
filename = 'favorite_number.json'

# Menggunakan json.dumps() untuk menyimpan angka ke dalam file
with open(filename, 'w') as file_object:
    json.dump(favorite_number, file_object)

print(f"Terima kasih! Angka favorit Anda telah disimpan.")