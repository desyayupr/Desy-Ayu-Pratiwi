def make_album(artist_name, album_title, songs=None):
    """Membangun dictionary yang mendeskripsikan informasi album musik."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    if songs:
        album['total_songs'] = songs
    return album

print("--- 🎵 Program Pendataan Album Musik Interaktif ---")
print("Ketik 'quit' kapan saja jika ingin keluar.\n")

# Menggunakan while loop untuk input interaktif
while True:
    artist = input("Masukkan nama artis: ")
    if artist.lower() == 'quit':
        break
        
    title = input("Masukkan judul album: ")
    if title.lower() == 'quit':
        break
        
    # Memanggil fungsi make_album dan menyimpan hasilnya
    user_album = make_album(artist, title)
    
    print("\nDictionary album yang berhasil dibuat:")
    print(user_album)
    print("-" * 45)

print("\nTerima kasih telah menggunakan program pendataan album!")