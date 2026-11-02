# membuat daftar makanan favprit
makanan = ["Nasi goreng","Dimsum","Bakso"]

# mencoba mengakses indeks 5, padahal didalam list hanya ada ada indeks 0, 1, 2
# hal tersebut dapat menyebabkan error
print(makanan[5]) # ini ketika di run akan error, maka solusinya adalah

# memperbaiki error dengan memanggil indeks yang benar 
print(makanan[0]) # makan ketika di run akan muncul "Nasi goreng"