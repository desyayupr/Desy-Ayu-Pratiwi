# membuat daftar kosong untuk menyimpan hasil kubus 
cubes = []

# menggunakan for loop untuk menghitung kubus dari angka 1-10
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
    
# menggunakan for loop untuk mencetak setiap nilai didalam daftar cube
for cube in cubes:
    print(cube)
    
# noted:
# **3 artinya dipangkatkan 3