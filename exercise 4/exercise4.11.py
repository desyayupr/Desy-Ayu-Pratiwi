# List pizza awal
pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Membuat salinan list menggunakan slice [:]
friend_pizzas = pizzas[:]

# Menambahkan pizza baru ke list asli
pizzas.append('bbq chicken')

# Menambahkan pizza berbeda ke list teman
friend_pizzas.append('four cheese')

# Menampilkan pizza favorit saya
print("Pizza favorit saya adalah:")
for pizza in pizzas:
    print(f"- {pizza}")

# Menampilkan pizza favorit teman saya
print("\nPizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
    
# Maksud dari membuat salinan list menggunakan slice [:] adalah untuk menyalin isi data dari suatu list ke variabel baru secara mandiri, sehingga kedua list tersebut berdiri sendiri dan tidak saling memengaruhi.