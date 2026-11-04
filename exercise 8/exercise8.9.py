# 1. Membuat list yang berisi daftar pesan teks singkat
text_messages = [
    "Halo, apa kabar?", 
    "Jangan lupa belajar Python hari ini ya.", 
    "Meeting project akan dimulai jam 2 siang.", 
    "Sampai jumpa nanti!"
]

# 2. Mendefinisikan fungsi show_messages() yang menerima sebuah parameter berupa list
def show_messages(messages):
    """Mencetak setiap pesan teks yang ada di dalam list."""
    print("--- DAFTAR PESAN MASUK ---")
    for message in messages:
        print(f"- {message}")

# 3. Memanggil fungsi dan mengirimkan list text_messages sebagai argumen
show_messages(text_messages)