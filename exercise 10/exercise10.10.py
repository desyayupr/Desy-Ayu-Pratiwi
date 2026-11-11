def count_common_words(filename, word):
    """Membaca file teks dan menghitung kemunculan suatu kata di dalamnya."""
    try:
        with open(filename, 'r', encoding='utf-8') as file_object:
            contents = file_object.read()
            
    except FileNotFoundError:
        print(f"Maaf, file '{filename}' tidak ditemukan.")
    else:
        # Mengubah teks ke huruf kecil agar pencarian lebih akurat
        # Menghitung kemunculan kata 'the' secara utuh maupun bagian dari kata lain
        count_general = contents.lower().count(word)
        print(f"Kata '{word}' (termasuk di dalam 'then', 'there', dll) muncul sebanyak: {count_general} kali.")
        
        # Mencoba menghitung dengan spasi di belakangnya ('the ') untuk aproksimasi yang lebih spesifik
        word_with_space = f"{word} "
        count_specific = contents.lower().count(word_with_space)
        print(f"Kata '{word} ' (dengan spasi di belakang) muncul sebanyak: {count_specific} kali.")

# Contoh penggunaan (pastikan file teks sudah tersedia di direktori kamu)
filename = 'alice.txt'  # Contoh nama file teks dari Project Gutenberg
count_common_words(filename, 'the')