# membuat list berisi nama-nama sungai
sungai = ["Nil", "Amazon", "Danube", "Mississippi"]
print("Daftar sungai awal:", sungai)

# 1. len(), menghitung jumlah item dalam list
print("Jumlah sungai dalam daftar:", len(sungai))

# 2. append(), menambahkan item di akhir daftar
sungai.append("Mekong")
print("Setelah menggunakan sungai.append():", sungai)

# 3. insert(), menambahkan item pada posisi indeks tertentu
sungai.insert(2, "Ganges")
print("Setelah menggunakan sungai.insert():", sungai)

# 4. del, menghapus item berdasarkan posisi indeks
del sungai[1]
print("Setelah menggunakan del:", sungai)

# 5. pop(), menghapus item terakhir dari daftar dan menyimpannya (bisa digunakan kembali)
sungai_terakhir = sungai.pop()
print(f"Sungai yang dihapus dengan pop(): {sungai_terakhir}")
print("Setelah menggunakan pop():", sungai)

# 6. remove(), menghapus item berdasarkan nilai/nama isinya
print("Daftar terurut sementara (sorted):", sorted(sungai))
print("Daftar asli setelah sorted() (tidak berubah):", sungai)

# 8. reverse(), membalik urutan daftar secara permanen
sungai.reverse()
print("Setelah menggunakan reverse():", sungai)

# kembalikan urutannya seperti semula agar rapi untuk pengujian berikutnya
sungai.reverse()

# 9. sort(), mengurutkan daftar secara permanen sesuai abjad (A-Z)
sungai.sort()
print("Setelah menggunakan sort() (A-Z):", sungai)

# 10. sort(reverse-True), mengurutkan daftar secara permanen berlawanan abjad (Z-A)
sungai.sort(reverse=True)
print("Setelah menggunakan sort(reverse=True) (Z-A):", sungai)