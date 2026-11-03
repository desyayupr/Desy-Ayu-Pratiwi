# 1. Membuat list berisi tiga buah kesukaan
favorite_fruits = ['banana', 'apple', 'strawberry']

# 2. Membuat lima pernyataan if independen
if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'orange' in favorite_fruits:
    print("You really like oranges!")

if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")

if 'grape' in favorite_fruits:
    print("You really like grapes!")
    
# 'if' independen (terpisah) berbeda dengan struktur if-elif-else
# 'if' terpisah akan mengecek semuanya satu per satu secara mandiri
# karena 'banana', 'apple', dan 'strawberry' ada dalam list, maka akan tercetak.
# 'orange' dan 'grape' karena tidak ada dalam list maka pernyataan 'if' tersebut bernilai 'false'