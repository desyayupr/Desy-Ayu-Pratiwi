# kumpulan program di bab 4 sesuai PEP 8

# exercise4.1.py
# membuat daftar pizza favorit
pizzas = ["pepperoni", "meat lover", "cheese"]

# menggunakan 4 spasi untuk indentasi
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
    
# menambahkan baris di luar for loop yang menyatakan seberapa besar kesukaannya dengan pizza
print(f"\nI really love pizza!")

# exercise4.3.py
# menggunakan for loop dan range (1, 21) untuk mencetak angka 1-20
for angka in range(1, 21):
    print(angka)
    
# exercise4.6.py
# membuat list angka ganjil 1-20
odd_numbers = list(range(1, 21, 2))

for angka in odd_numbers:
    print(angka)
    
# indentasi : setiap blok perulangan (for) menjorok ke dalam menggunakan empat spasi
# panjang baris : tidak boleh lebih dari 80 
# baris kosong : tidak menggunakan baris kosong secara berlebihan
