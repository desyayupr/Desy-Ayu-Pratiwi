# 1. Dictionary yang menyimpan data orang dan bahasa pemrograman favorit mereka
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 2. List berisi orang-orang yang harus/diminta mengikuti polling
# (Beberapa nama sudah ada di dictionary, beberapa belum)
coders_to_poll = ['jen', 'sarah', 'budi', 'edward', 'siti']

# 3. Melakukan perulangan untuk mengecek status mereka
for coder in coders_to_poll:
    # Memeriksa apakah nama tersebut sudah ada di dalam keys dictionary favorite_languages
    if coder in favorite_languages:
        print(f"Terima kasih {coder.title()}, karena sudah meluangkan waktu untuk mengikuti polling.")
    else:
        print(f"Halo {coder.title()}, Anda diundang untuk mengikuti polling bahasa pemrograman favorit kami.")
        
# if coder in favprite_languages: digunakan untuk mengecek apakah sebuah nama ada dalam daftar kunci (keys) 