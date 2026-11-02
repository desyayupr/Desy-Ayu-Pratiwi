# list nama teman dari latihan exercise3.6.py
nama = ["Berlina", "Yusrina", "Windi", "Vrysa", "Djilva", "Tea", "Nayla", "Kala"]

# print pesan bahwa hanya mengundang 2 orang
print(f"Mohon maaf, saya hanya dapat mengundang 2 orang untuk bergabung makan malam pada hari ini")

# gunakan pop( untuk menghapus nama teman satu per satu dan mengirim pesan permintaan maaf)
popped_nama = nama.pop()
print(F"Maaf {popped_nama}, saya terpaksa membatalkan undangan makan malam pada hari ini")

popped_nama = nama.pop()
print(F"Maaf {popped_nama}, saya terpaksa membatalkan undangan makan malam pada hari ini")

popped_nama = nama.pop()
print(F"Maaf {popped_nama}, saya terpaksa membatalkan undangan makan malam pada hari ini")

popped_nama = nama.pop()
print(F"Maaf {popped_nama}, saya terpaksa membatalkan undangan makan malam pada hari ini")

popped_nama = nama.pop()
print(F"Maaf {popped_nama}, saya terpaksa membatalkan undangan makan malam pada hari ini")

popped_nama = nama.pop()
print(F"Maaf {popped_nama}, saya terpaksa membatalkan undangan makan malam pada hari ini")

# pesan untuk dua orang tersisa
print(f"\nKepada {nama[0]}, Anda masih diundang untuk makan malam pada hari ini")
print(f"Kepada {nama[1]}, Anda masih diundang untuk makan malam pada hari ini")

# gunakan del untuk menghapus dua nama terakhir pada list
del nama[0]
del nama[0] # indeks ke-0 bergeser otomatis setelah elemen utama terhapus

print("\nIsi list akhir:", nama)
