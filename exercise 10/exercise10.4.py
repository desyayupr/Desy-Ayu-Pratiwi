# Menentukan nama file tujuan
filename = 'guest.txt'

# Meminta pengguna memasukkan nama mereka
name = input("Masukkan nama Anda: ")

# Membuka file dalam mode 'w' (write) untuk menulis data ke file
with open(filename, 'w') as file_object:
    file_object.write(name)

print(f"Nama '{name}' telah berhasil disimpan ke dalam file {filename}.")