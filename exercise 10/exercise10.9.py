def read_pet_file(filename):
    """Mencoba membaca file hewan dan gagal secara senyap jika file tidak ada."""
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
            print(f"\n--- Isi dari file {filename} ---")
            print(contents.strip())
            
    except FileNotFoundError:
        # Gagal secara senyap menggunakan pass, tanpa mencetak pesan error apa pun
        pass

# Daftar file yang akan dibaca oleh program
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    read_pet_file(filename)