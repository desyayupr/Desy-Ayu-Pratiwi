# 1. Membuat list awal berisi daftar pesan teks
text_messages = [
    "Halo, apa kabar?", 
    "Jangan lupa belajar Python hari ini ya.", 
    "Meeting project akan dimulai jam 2 siang.", 
    "Sampai jumpa nanti!"
]

# Membuat list kosong untuk menampung pesan yang dikirim
sent_messages = []

# 2. Mendefinisikan fungsi send_messages()
def send_messages(messages, sent):
    """Mencetak setiap pesan dan memindahkannya ke list sent_messages."""
    print("--- 🚀 SEDANG MENGIRIM PESAN ---")
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: '{current_message}'")
        sent.append(current_message)

# 3. Memanggil fungsi dengan mengirimkan SALINAN list menggunakan irisan [:]
# Ini membuat list asli (text_messages) tetap aman dan utuh
send_messages(text_messages[:], sent_messages)

# 4. Mencetak kedua list untuk membuktikan list asli tidak berubah
print("\n--- STATUS AKHIR LIST (SETELAH FUNGSI DIPANGGIL) ---")
print(f"List asli (text_messages): {text_messages}")
print(f"List tujuan (sent_messages): {sent_messages}")