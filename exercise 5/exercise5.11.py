# 1. Menyimpan angka 1 sampai 9 dalam sebuah list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. Melakukan loop melalui list tersebut
for number in numbers:
    # 3. Menggunakan if-elif-else chain untuk menentukan akhiran ordinal
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
        
# for number in bumbers: mengambil setiap angka satu per satu dari dalam list