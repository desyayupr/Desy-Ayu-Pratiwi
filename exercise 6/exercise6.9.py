# 1. Membuat dictionary favorite_places dengan list di dalam values
favorite_places = {
    'budi': ['pantai kuta', 'gunung merbabu', 'candi borobudur'],
    'siti': ['jalan malioboro', 'pantai parangtritis'],
    'andi': ['kepulauan raja ampat']
}

# 2. Melakukan perulangan (loop) untuk mengakses nama dan daftar tempat favorit
for name, places in favorite_places.items():
    print(f"\nTempat-tempat favorit {name.title()} adalah:")
    
    # Karena places adalah list, kita buat perulangan lagi di dalam loop utama (nested loop)
    for place in places:
        print(f"- {place.title()}")
    