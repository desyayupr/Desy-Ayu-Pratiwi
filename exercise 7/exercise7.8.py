# 1. Membuat list pesanan sandwich dan list kosong untuk sandwich yang sudah jadi
sandwich_orders = ['tuna', 'turku', 'roast beef', 'keju', 'ayam']
finished_sandwiches = []

# 2. Menggunakan while loop untuk memproses setiap pesanan sampai list kosong
while sandwich_orders:
    # Mengambil dan menghapus pesanan pertama dari list sandwich_orders menggunakan pop()
    current_sandwich = sandwich_orders.pop(0)
    
    print(f"Saya sedang membuat {current_sandwich} sandwich Anda.")
    
    # 3. Memindahkan sandwich yang sudah dibuat ke list finished_sandwiches
    finished_sandwiches.append(current_sandwich)

# 4. Setelah semua selesai, cetak daftar sandwich yang sudah dibuat
print("\nSemua sandwich berikut telah selesai dibuat:")
for finished in finished_sandwiches:
    print(f"- {finished.title()} sandwich")
    
# Fungsi .pop(0) mengambil elemen pertama dari dalam list sandwich_orders sekaligus menghapusnya dari list tersebut agar perulangan bisa terus berlanjut hingga list-nya habis (kosong).