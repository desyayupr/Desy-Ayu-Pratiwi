# membuat list angka ganjil 1-20
# range(start, stop, step) -> mulai dari 1, berhenti sebelum 21, dengan kelipatan 2

odd_numbers = list(range(1, 21, 2))
# itu kelipatan 2 maksudnya melompat 2 angka sehingga menghasilkan deretan: 1,3,5,7,9,dst

# menggunakan for loop unutk mencetak setiap angka ganjil
for angka in odd_numbers:
    print(angka)