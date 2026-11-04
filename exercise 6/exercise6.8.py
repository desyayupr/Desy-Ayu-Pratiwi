# 1. Membuat dictionary untuk masing-masing hewan peliharaan
pet_1 = {
    'kind': 'kucing',
    'owner': 'budi',
}

pet_2 = {
    'kind': 'anjing',
    'owner': 'siti',
}

pet_3 = {
    'kind': 'burung kakaktua',
    'owner': 'andi',
}

pet_4 = {
    'kind': 'hamster',
    'owner': 'ani',
}

# 2. Menyimpan semua dictionary ke dalam list bernama pets
pets = [pet_1, pet_2, pet_3, pet_4]

# 3. Melakukan loop pada list pets dan mencetak informasi setiap hewan
for pet in pets:
    animal_kind = pet['kind']
    owner_name = pet['owner']
    
    print(f"Informasi Hewan Peliharaan:")
    print(f"- Jenis Hewan : {animal_kind.title()}")
    print(f"- Nama Pemilik: {owner_name.title()}")
    print("-" * 25)  
    
# kurung siku [] digunakan untuk mengakses elemen berdasarkan key (pada dictionary) atau berdasarkan indeks angka (pada list)
# contoh: pet['kind] atau people[0]