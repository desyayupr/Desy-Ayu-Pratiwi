# 1. Membuat list sandwich_orders dengan 'pastrami' muncul minimal 3 kali
sandwich_orders = ['tuna', 'pastrami', 'turku', 'pastrami', 'roast beef', 'pastrami', 'keju']
finished_sandwiches = []

# 2. Memberitahu pengguna bahwa deli kehabisan pastrami
print("Mohon maaf, toko deli sedang kehabisan stok pastrami hari ini!\n")

# 3. Menggunakan while loop untuk menghapus SEMUA kemunculan 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 4. Memproses sisa pesanan sandwich yang ada
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya sedang membuat {current_sandwich} sandwich Anda.")
    
    # Memindahkan sandwich yang sudah dibuat ke list finished_sandwiches
    finished_sandwiches.append(current_sandwich)

# 5. Menampilkan daftar akhir sandwich yang berhasil dibuat
print("\nSemua sandwich berikut telah selesai dibuat:")
for finished in finished_sandwiches:
    print(f"- {finished.title()} sandwich")