# 1. Mendefinisikan fungsi dengan satu parameter 'title'
def favorite_book(title):
    """Menampilkan pesan tentang buku favorit."""
    print(f"One of my favorite books is {title.title()}.")

# 2. Memanggil fungsi dengan menyertakan argumen judul buku
favorite_book('alice in wonderland')

# diberi (title) karena fungsi ini bertindak seperti cetakan kosong.
# fungsi tersebut bisa menerima masukan dari luar, sehingga output sesuai data yang diinputkan
# misal :
# def favorite_book(title):
#    print(f"One of my favorite books is {title.title()}.")

# Pemanggilan dengan argumen yang berbeda-beda:
# favorite_book('alice in wonderland')  # Hasil: One of my favorite books is Alice In Wonderland.
# favorite_book('python crash course') # Hasil: One of my favorite books is Python Crash Course.
# favorite_book('atomic habits')       # Hasil: One of my favorite books is Atomic Habits.