# Menentukan nama file buku tamu
filename = 'guest_book.txt'

print("--- Buku Tamu (Ketik 'keluar' atau 'quit' untuk berhenti) ---")

# Membuka file dalam mode 'a' (append) agar data baru ditambahkan tanpa menghapus data sebelumnya
with open(filename, 'a') as file_object:
    while True:
        name = input("\nMasukkan nama Anda: ")
        
        # Kondisi untuk menghentikan perulangan jika pengguna ingin keluar
        if name.lower() in ['keluar', 'quit', 'exit']:
            print("Terima kasih! Program buku tamu ditutup.")
            break
            
        # Menulis nama ke file disertai karakter baris baru (\n)
        file_object.write(f"{name}\n")
        print(f"Halo {name}, kunjungan Anda telah dicatat di buku tamu!")