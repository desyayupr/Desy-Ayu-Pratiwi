from user import User

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