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


class Admin(User):
    """Represent an administrator, a specialized kind of user."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize attributes of an admin."""
        super().__init__(first_name, last_name, username, email, location)
        # Atribut privileges yang menyimpan daftar string hak akses
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify content",
        ]

    def show_privileges(self):
        """Display the administrator's set of privileges."""
        print(f"\nDaftar Hak Akses (Privileges) untuk Admin {self.username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# 1. Membuat instance (objek) dari kelas Admin
admin_user = Admin(
    "Joko", "Santoso", "admin_joko", "joko.admin@email.com", "Surakarta"
)

# 2. Memanggil metode show_privileges()
admin_user.show_privileges()

# (Opsional) Memanggil metode bawaan dari kelas induk (User)
admin_user.describe_user()
admin_user.greet_user()