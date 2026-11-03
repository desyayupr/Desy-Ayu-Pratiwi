# Menentukan daftar makanan saya dan makanan teman
my_foods = ['pizza', 'falafel', 'kue wortel']
friend_foods = my_foods[:]

# Menambahkan makanan baru ke masing-masing list
my_foods.append('cannoli')
friend_foods.append('es krim')

# Mencetak list makanan saya dengan for loop
print("Makanan favorit saya adalah:")
for food in my_foods:
    print(f"- {food}")

# Mencetak list makanan teman dengan for loop
print("\nMakanan favorit teman saya adalah:")
for food in friend_foods:
    print(f"- {food}")
    
# menggunakan perulangan for ganda, maksudnya adalah menggunakan dua loop for berurutan untuk memproses dua list yang berbeda secara mandiri.