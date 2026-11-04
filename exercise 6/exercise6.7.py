# 1. Membuat dictionary untuk orang pertama (dari Latihan 6-1)
person_1 = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 22,
    'city': 'Surakarta',
}

# 2. Membuat dua dictionary baru untuk orang kedua dan ketiga
person_2 = {
    'first_name': 'Siti',
    'last_name': 'Rahma',
    'age': 25,
    'city': 'Yogyakarta',
}

person_3 = {
    'first_name': 'Andi',
    'last_name': 'Pratama',
    'age': 20,
    'city': 'Bandung',
}

# 3. Menyimpan semua dictionary ke dalam sebuah list bernama people
people = [person_1, person_2, person_3]

# 4. Melakukan loop pada list people dan mencetak informasi setiap orang
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"Nama : {full_name}")
    print(f"Usia : {age} tahun")
    print(f"Kota : {city}")
    print("-" * 20)  