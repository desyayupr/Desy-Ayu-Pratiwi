class User:
    """A simple model representing a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"- Username : {self.username}")
        print(f"- Email    : {self.email}")
        print(f"- Lokasi   : {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Halo, {self.first_name}! Senang bisa melihatmu kembali.")


# 1. Membuat beberapa instance (objek) yang merepresentasikan pengguna berbeda
user1 = User("Budi", "Santoso", "budisantosa", "budi@email.com", "Surakarta")
user2 = User("Siti", "Rahma", "sitirahma", "siti@email.com", "Yogyakarta")
user3 = User("Andi", "Pratama", "andipratama", "andi@email.com", "Bandung")

# 2. Memanggil kedua metode untuk setiap pengguna
users = [user1, user2, user3]

for u in users:
    u.describe_user()
    u.greet_user()
    
# __init__: itu inisialisasi, dia berisi apapun yang diminta di awal
# greet_user(): mencetak pesan sapaan personal