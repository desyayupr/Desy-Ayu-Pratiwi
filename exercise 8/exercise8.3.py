# 1. Mendefinisikan fungsi dengan dua parameter: size dan text
def make_shirt(size, text):
    """Menampilkan ringkasan ukuran dan teks pada kaos."""
    print(f"\nMembuat kaos ukuran {size.upper()} dengan tulisan: '{text}'.")

# 2. Pemanggilan pertama menggunakan Positional Arguments (berurutan berdasarkan posisi)
make_shirt('L', 'Python is Life')

# 3. Pemanggilan kedua menggunakan Keyword Arguments (menyebutkan nama parameternya secara langsung)
make_shirt(size='M', text='Keep Coding!')