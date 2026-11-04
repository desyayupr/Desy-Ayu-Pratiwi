# Versi 1: Menggunakan Tes Kondisi pada Pernyataan while (while conditional test)
prompt = "\nMasukkan topping pizza Anda"
prompt += "\n(Ketik 'quit' untuk berhenti): "

topping = ""
# Loop berjalan selama nilai variabel topping TIDAK SAMA DENGAN 'quit'
while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"Menambahkan {topping} ke pizza Anda!")

print("\nPizza Anda sedang disiapkan!")

# Versi 2: Menggunakan Variabel Aktif / Flag (active variable)
prompt = "\nMasukkan topping pizza Anda"
prompt += "\n(Ketik 'quit' untuk berhenti): "

# Membuat variabel penanda (flag) dengan status aktif (True)
active = True

while active:
    topping = input(prompt)
    
    if topping == 'quit':
        # Mengubah status flag menjadi False untuk menghentikan loop
        active = False
    else:
        print(f"Menambahkan {topping} ke pizza Anda!")

print("\nPizza Anda sedang disiapkan!")

# Versi 3: Menggunakan Pernyataan break (break statement)
prompt = "\nMasukkan topping pizza Anda"
prompt += "\n(Ketik 'quit' untuk berhenti): "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        # Keluar secara paksa dari loop seketika pengguna mengetik 'quit'
        break
    else:
        print(f"Menambahkan {topping} ke pizza Anda!")

print("\nPizza Anda sedang disiapkan!")