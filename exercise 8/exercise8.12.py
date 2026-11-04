# 1. Mendefinisikan fungsi menggunakan parameter *items (arbitrary arguments)
def make_sandwich(*items):
    """Mencetak ringkasan bahan-bahan sandwich yang dipesan."""
    print("\n--- PESANAN SANDWICH ---")
    print("Membuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"- {item}")

# 2. Memanggil fungsi sebanyak tiga kali dengan jumlah argumen yang berbeda
make_sandwich('keju', 'tomat', 'selada')
make_sandwich('daging sapi', 'keju cheddar')
make_sandwich('telur ceplok', 'mayones', 'saus sambal', 'mentimun')