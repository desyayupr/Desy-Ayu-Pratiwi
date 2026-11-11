def read_pet_file(filename):
    """Mencoba membaca file hewan dan mencetak isinya ke layar."""
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
            print(f"\n--- Isi dari file {filename} ---")
            print(contents.strip())
            
    except FileNotFoundError:
        # Menampilkan pesan ramah jika file tidak ditemukan
        print(f"\n[Peringatan] Maaf, file '{filename}' tidak dapat ditemukan di direktori ini.")

# Daftar file yang akan dibaca oleh program
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    read_pet_file(filename)