import json

filename = 'user_info.json'

# 1. Meminta input dan menyimpannya ke dalam dictionary
print("Silakan masukkan beberapa informasi tentang diri Anda:")
user_info = {
    'username': input("Nama Anda: "),
    'hobby': input("Hobi Anda: "),
    'language': input("Bahasa pemrograman favorit Anda: ")
}

# 2. Menulis dictionary ke file menggunakan json.dumps()
# json.dumps() mengubah objek Python menjadi string berformat JSON
json_string = json.dumps(user_info)
with open(filename, 'w') as f:
    f.write(json_string)

print("\nData Anda telah berhasil disimpan!")

# 3. Membaca kembali isi file menggunakan json.loads()
with open(filename, 'r') as f:
    contents = f.read()
    # json.loads() mengubah string JSON kembali menjadi dictionary Python
    recovered_info = json.loads(contents)

# 4. Menampilkan ringkasan informasi yang diingat program
print("\n--- Ringkasan yang Diingat Program ---")
print(f"Nama: {recovered_info['username']}")
print(f"Hobi: {recovered_info['hobby']}")
print(f"Bahasa Pemrograman Favorit: {recovered_info['language']}")