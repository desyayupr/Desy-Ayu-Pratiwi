# 1. Membuat variabel prompt untuk instruksi
prompt = "\nMasukkan topping pizza yang Anda inginkan"
prompt += "\n(Ketik 'quit' jika sudah selesai): "

# 2. Menggunakan while loop untuk meminta input secara berulang
while True:
    topping = input(prompt)
    
    # 3. Memeriksa apakah pengguna ingin keluar dari loop
    if topping == 'quit':
        print("\nTerima kasih! Pizza Anda sedang disiapkan.")
        break
    else:
        print(f"Menambahkan {topping} ke pizza Anda!")
        
# menggunakan while True agar program terus berjalan menerima input berkali-kali