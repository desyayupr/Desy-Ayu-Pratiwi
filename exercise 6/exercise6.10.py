# 1. Memodifikasi dictionary favorite_numbers dengan list di dalam values
favorite_numbers = {
    'budi': [7, 14, 21],
    'siti': [12, 5],
    'andi': [3, 9, 27, 33],
    'ani': [8],
    'eka': [10, 20]
}

# 2. Melakukan perulangan untuk mengakses nama dan daftar angka favorit
for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()} adalah:")
    
    # Karena numbers adalah list, kita buat nested loop untuk mencetak angkanya satu per satu
    for number in numbers:
        print(f"- {number}")
        
# perulangan bersarang (nested loop):
# perulangan luar (for name, numbers in favorite_numbers.items(): ) mengambil nama dan kumpulan angkanya.
# perulangan dalam (for number in numbers) menguraikan isi list angka tersebut agar tercetak rapi ke bawah.