import json

def get_stored_username(filename):
    """Ambil username tersimpan jika ada."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    """Minta username baru dan simpan ke file."""
    username = input("Siapa nama Anda? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Sapa pengguna, verifikasi apakah username sudah benar, 
    atau minta yang baru jika tidak sesuai."""
    filename = 'username.json'
    username = get_stored_username(filename)
    
    if username:
        # Latihan 10-14: Verifikasi username
        verify = input(f"Apakah ini username Anda: {username}? (y/n): ")
        if verify.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(filename)
            print(f"Kami akan mengingat Anda saat kembali, {username}!")
    else:
        username = get_new_username(filename)
        print(f"Kami akan mengingat Anda saat kembali, {username}!")

greet_user()