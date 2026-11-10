from random import choice

# 1. Membuat list yang berisi rangkaian 10 angka dan 5 huruf
lottery_pool = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 'a', 'b', 'c', 'd', 'e']

# 2. Memilih 4 elemen secara acak dari list tersebut
# Kita menggunakan sample() atau perulangan dengan choice() agar tidak duplikat
winning_ticket = []
while len(winning_ticket) < 4:
    picked_item = choice(lottery_pool)
    
    # Memastikan elemen yang sama tidak dipilih dua kali
    if picked_item not in winning_ticket:
        winning_ticket.append(picked_item)

# 3. Mencetak pesan pemenang sesuai instruksi soal
print("--- Simulasi Undian (Lottery) ---")
print(f"Kombinasi angka atau huruf pemenang adalah: {winning_ticket}")
print("Pesan: Tiket apa pun yang cocok dengan 4 angka atau huruf ini memenangkan hadiah!")