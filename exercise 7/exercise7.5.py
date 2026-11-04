# 1. Membuat variabel instruksi untuk pengguna
prompt = "\nMasukkan usia Anda"
prompt += "\n(Ketik 'quit' jika sudah selesai): "

# 2. Menggunakan while loop untuk meminta input secara berulang
while True:
    age_input = input(prompt)
    
    # Memeriksa apakah pengguna ingin keluar dari program
    if age_input.lower() == 'quit':
        print("\nTerima kasih telah menggunakan layanan pemesanan tiket kami!")
        break
        
    # Mengubah input usia menjadi integer (angka bulat)
    age = int(age_input)
    
    # 3. Menentukan harga tiket berdasarkan ketentuan usia
    if age < 3:
        print("-> Tiket Anda gratis!")
    elif age <= 12:
        print("-> Harga tiket Anda adalah $10.")
    else:
        print("-> Harga tiket Anda adalah $15.")