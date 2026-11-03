# 1. Menyimpan lima makanan dasar ke dalam sebuah tuple
menu_makanan = ('ayam goreng', 'nasi putih', 'sup sayur', 'ikan bakar', 'tahu tempe')

# Menggunakan for loop untuk mencetak setiap makanan yang ditawarkan restoran
print("Menu asli restoran (Buffet):")
for makanan in menu_makanan:
    print(f"- {makanan}")

# 2. memodifikasi salah satu item (baris ini akan memicu error jika dijalankan)
# Python akan menolak karena tuple bersifat immutable (tidak bisa diubah isinya)
# menu_makanan[0] = 'bebek goreng'  # <-- Uncomment baris ini untuk melihat error TypeError

# 3. Restoran mengubah menu, mengganti dua item dengan makanan baru
# menulis ulang variabel tuple dengan isi yang baru
menu_makanan = ('bebek goreng', 'nasi putih', 'sate ayam', 'ikan bakar', 'tahu tempe')

# Menggunakan for loop untuk mencetak menu yang sudah direvisi
print("\nMenu revisi restoran (Buffet):")
for makanan in menu_makanan:
    print(f"- {makanan}")
    
