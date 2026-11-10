class User:
    """A simple model representing a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize user attributes, including login_attempts."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Atribut dengan nilai default 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"- Username : {self.username}")
        print(f"- Email    : {self.email}")
        print(f"- Lokasi   : {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Halo, {self.first_name}! Senang bisa melihatmu kembali.")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0


# Membuat instance dari kelas User
user = User("Budi", "Santoso", "budisantosa", "budi@email.com", "Surakarta")

# Memanggil increment_login_attempts() beberapa kali
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Mencetak nilai login_attempts
print(f"Jumlah percobaan login (setelah ditambah): {user.login_attempts}")

# Memanggil reset_login_attempts()
user.reset_login_attempts()

# Mencetak kembali untuk memastikan nilainya kembali menjadi 0
print(f"Jumlah percobaan login (setelah direset): {user.login_attempts}")