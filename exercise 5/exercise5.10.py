# 1. Membuat list current_users
current_users = ['admin', 'jaden', 'sarah', 'eric', 'alice']

# 2. Membuat list new_users (beberapa nama sama dengan current_users, dengan variasi huruf besar/kecil)
new_users = ['Jaden', 'bob', 'SARAH', 'david', 'charlie']

# 3. Membuat list berisi versi huruf kecil (lowercase) dari current_users untuk pengecekan case-insensitive
current_users_lower = [user.lower() for user in current_users]

# 4. Melakukan loop pada new_users untuk memeriksa ketersediaan username
for new_user in new_users:
    # Memeriksa apakah versi lowercase dari new_user ada di dalam current_users_lower
    if new_user.lower() in current_users_lower:
        print(f"Maaf, username '{new_user}' sudah digunakan. Anda harus memasukkan username baru.")
    else:
        print(f"Selamat, username '{new_user}' tersedia.")
        
# list comprehension([user.lower() for user in current_users]): digunakan untuk mengubah seluruh isi list di current_users menjadi huruf kecil otomatis
# perbedaan huruf kapital tidak akan menjadi masalah