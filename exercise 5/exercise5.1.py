# variabel awal
car = "subaru"
number = 15
color = "red"

# 5 pengujian yang bernilai true

# test 1: kesetaraan string (True)
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

# test 2: ketidaksamaan string (True)
print("\nIs car != 'audi'? I predict True.")

# test 3: pengujian metode huruf kecil/lower() (True)
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == "subaru")

# test 4: perbandingan angka lebih besar (True)
print("\nIs number > 10? I predict True.")
print(number > 10)

# test 5: pengecekan anggota dalam list (True)
colors = ["red", "greean","blue"]
print("\nIs 'red' in colors? I predict True")
print("red" in colors)

# 5 pengujian yang bernilai false
# test 6: keetaraan string yang salah (False)
print("\nIs car == 'toyota'? I predict False.")
print(car == "toyota")

# test 7: sensitif terhadap huruf kapital (False)
print("\nIs car == 'Subaru'? I predict False.")
print(car == "Subaru")

# test 8: perbandingan angka kurang dari (False)
print("\nIs  number < 5? I predict False.")
print(number < 5)

# test 9: kesetaraan angka yang salah (False)
print("\nIs number == 20? I predict False.")
print(number == 20)

# test 10: pengecekan anggota list yang tidak ada (False)
print("\nIs 'yellow' in colors? I predict False.")
print("yellow" in colors)

# noted:
# conditional test: setiap perbandingan di python akan dievaluasi menjadi nilai boolean yaitu True atau False
# == (sama dengan)
# != (tidak sama dengan)
# > , < (lebih/kurang dari)
# in (memeriksa apakah suatu nilai ada didalam list)
  