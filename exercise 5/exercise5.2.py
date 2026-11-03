# 1. Tests kesetaraan dan ketidaksamaan dengan string (teks)
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False


# 2. Tests menggunakan method lower() (mengabaikan huruf besar/kecil)
user_name = 'Admin'
print("\nIs user_name.lower() == 'admin'? I predict True.")
print(user_name.lower() == 'admin')  # True

print("\nIs user_name == 'admin'? I predict False.")
print(user_name == 'admin')  # False


# 3. test numerik (angka): kesetaraan, ketidaksamaan, lebih dari, kurang dari, dll.
age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)  # True

print("\nIs age != 30? I predict True.")
print(age != 30)  # True

print("\nIs age > 20? I predict True.")
print(age > 20)  # True

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

print("\nIs age >= 30? I predict False.")
print(age >= 30)  # False

print("\nIs age <= 20? I predict False.")
print(age <= 20)  # False


# 4. test menggunakan keyword 'and' dan 'or'
age_0 = 22
age_1 = 18

print("\nIs age_0 >= 21 and age_1 >= 21? I predict False.")
print(age_0 >= 21 and age_1 >= 21)  # False (karena salah satu False)

print("\nIs age_0 >= 21 or age_1 >= 21? I predict True.")
print(age_0 >= 21 or age_1 >= 21)  # True (karena salah satu True)


# 5. test apakah sutau item ada di dalam list (operator 'in')
requested_toppings = ['mushrooms', 'onions', 'pineapple']

print("\nIs 'mushrooms' in requested_toppings? I predict True.")
print('mushrooms' in requested_toppings)  # True

print("\nIs 'pepperoni' in requested_toppings? I predict False.")
print('pepperoni' in requested_toppings)  # False


# 6. test apakah suatu item tidak ada di dalam list (operator 'not in')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

print("\nIs 'marie' not in banned_users? I predict True.")
print(user not in banned_users)  # True

print("\nIs 'andrew' not in banned_users? I predict False.")
print('andrew' not in banned_users)  # False

# kesetaraan dan ketidaksamaan string (== dan !=)
# menggunakan == untuk mengecek apakah teks sama persis
# menggunakan != untuk mengecek apakah dua teks berbeda

# 'and' dan 'or'
# and: bernilai True hanya jika semua kondisi benar
# or: bernilai True jika setidaknya salah satu kondisi benar

# in: keberadaan item dalam list

# not in: ketidakberadaan item dalam list