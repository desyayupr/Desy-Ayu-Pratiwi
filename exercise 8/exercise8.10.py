# 1. Membuat list awal berisi daftar pesan teks
text_messages = [
    "Halo, apa kabar?", 
    "Jangan lupa belajar Python hari ini ya.", 
    "Meeting project akan dimulai jam 2 siang.", 
    "Sampai jumpa nanti!"
]

# Membuat list kosong untuk menampung pesan yang sudah dikirim
sent_messages = []

# 2. Mendefinisikan fungsi send_messages()
def send_messages(messages, sent):
    """Mencetak setiap pesan dan memindahkannya ke list sent_messages."""
    print("--- 🚀 SEDANG MENGIRIM PESAN ---")
    
    # Menggunakan while loop selama list messages masih ada isinya
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: '{current_message}'")
        sent.append(current_message)

# 3. Memanggil fungsi dengan mengirimkan kedua list sebagai argumen
send_messages(text_messages, sent_messages)

# 4. Mencetak kedua list untuk memverifikasi hasil pemindahan
print("\n--- 📋 STATUS AKHIR LIST ---")
print(f"List asli (text_messages): {text_messages}")
print(f"List tujuan (sent_messages): {sent_messages}")