# pembaruan untuk learning_c.py
filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object.read().splitlines(): # menggunakan fungsi splitlines() untuk memecah sebuah string (teks) menjadi daftar (list) yang berisi baris-baris terpisah, dengan mendeteksi karakter pemisah baris baru (newline seperti \n, \r\n, dll.) secara otomatis.
        modified_line = line.replace('Python', 'C')
        print(modified_line)