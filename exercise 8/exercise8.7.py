# 1. Mendefinisikan fungsi dengan parameter opsional 'songs = None'
def make_album(artist_name, album_title, songs=None):
    """Membangun dictionary yang mendeskripsikan informasi album musik."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    
    # Jika parameter songs diisi (tidak None), tambahkan ke dictionary
    if songs:
        album['total_songs'] = songs
        
    return album

# 2. Membuat tiga dictionary berbeda mewakili album musik
album1 = make_album('coldplay', 'A Head Full of Dreams')
album2 = make_album('taylor swift', '1989')
album3 = make_album('ed sheeran', 'divide')

# Mencetak hasil return value dari ketiga album pertama
print(album1)
print(album2)
print(album3)

# 3. Pemanggilan fungsi dengan menyertakan parameter opsional jumlah lagu
album_with_songs = make_album('queen', 'a night at the opera', songs=12)
print(album_with_songs)