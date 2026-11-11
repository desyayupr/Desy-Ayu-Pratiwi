import json

# Nama file tempat data JSON disimpan
filename = 'favorite_number.json'

try:
    # Membaca data dari file JSON
    with open(filename, 'r') as file_object:
        favorite_number = json.load(file_object)
except FileNotFoundError:
    print("File data tidak ditemukan.")
else:
    # Mencetak pesan sesuai instruksi soal
    print(f"I know your favorite number! It's {favorite_number}.")