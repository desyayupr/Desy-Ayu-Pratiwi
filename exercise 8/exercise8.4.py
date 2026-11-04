# 1. Mendefinisikan fungsi dengan nilai default pada parameter size dan text
def make_shirt(size='large', text='I love Python'):
    """Menampilkan ringkasan ukuran dan teks pada kaos."""
    print(f"\nMembuat kaos ukuran {size.upper()} dengan tulisan: '{text}'.")

# 2. Membuat kaos ukuran large dengan pesan default (tidak mengirim argumen apa pun)
make_shirt()

# 3. Membuat kaos ukuran medium dengan pesan default (mengisi argumen size saja)
make_shirt(size='medium')

# 4. Membuat kaos ukuran kecil (small) dengan pesan yang berbeda
make_shirt(size='small', text='Python Programmer in Training!')