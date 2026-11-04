# 1. Mendefinisikan fungsi menggunakan parameter **user_info (arbitrary keyword arguments)
def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi segala hal tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# 2. Memanggil fungsi dengan nama dan tiga informasi tambahan (key-value pairs)
user_profile = build_profile(
    'budi', 
    'santoso', 
    location='jakarta', 
    field='teknik industri', 
    hobby='pemrograman python'
)

# 3. Mencetak hasil dictionary profil yang terbentuk
print("--- PROFIL PENGGUNA ---")
print(user_profile)