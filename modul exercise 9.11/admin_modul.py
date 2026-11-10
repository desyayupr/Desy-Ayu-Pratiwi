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


class Privileges:
    """A class to store and display administrator privileges."""

    def __init__(self):
        """Initialize the privileges attribute with a list of strings."""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify content",
        ]

    def show_privileges(self):
        """Display the set of privileges."""
        print("Daftar Hak Akses (Privileges):")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an administrator, incorporating a Privileges instance."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize admin attributes, including a Privileges instance."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()