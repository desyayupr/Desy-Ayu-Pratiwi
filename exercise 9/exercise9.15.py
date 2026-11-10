from random import choice

def get_winning_ticket(lottery_pool):
    """Fungsi untuk menghasilkan kombinasi 4 angka/huruf pemenang secara acak."""
    winning_ticket = []
    while len(winning_ticket) < 4:
        picked_item = choice(lottery_pool)
        if picked_item not in winning_ticket:
            winning_ticket.append(picked_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """Mengecek apakah semua elemen di played_ticket ada di winning_ticket."""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

# 1. Daftar kumpuluan angka dan huruf (lottery pool)
lottery_pool = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 'a', 'b', 'c', 'd', 'e']

# 2. Membuat tiket pilihan kita sendiri (my_ticket)
my_ticket = [7, 2, 'a', 'e']

# 3. Melakukan loop sampai tiket kita cocok dengan pemenang
loops = 0
won = False

print("Sedang melakukan analisis undian, mohon tunggu sebentar...")

while not won:
    new_winning_ticket = get_winning_ticket(lottery_pool)
    loops += 1
    
    # Tiket menang jika seluruh isi my_ticket ada di dalam undian baru
    # (urutan bisa disesuaikan atau menggunakan pengecekan set)
    if set(my_ticket) == set(new_winning_ticket):
        won = True

# 4. Mencetak hasil laporan percobaan
print("\n--- Hasil Analisis Undian ---")
print(f"Tiket saya     : {my_ticket}")
print(f"Tiket pemenang : {new_winning_ticket}")
print(f"Jumlah percobaan (loop) yang dibutuhkan agar menang: {loops} kali.")