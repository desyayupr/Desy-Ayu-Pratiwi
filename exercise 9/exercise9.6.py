class Restaurant:
    """A model for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} saat ini sedang buka!")


class IceCreamStand(Restaurant):
    """Represent an ice cream stand, a specialized kind of restaurant."""

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """Initialize attributes of an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanila", "Cokelat", "Stroberi", "Matcha", "Mangga"]  # Atribut list rasa es krim

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"\nDaftar rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# 1. Membuat instance dari IceCreamStand
my_ice_cream_stand = IceCreamStand("Gelato Paradise")

# 2. Memanggil metode untuk menampilkan daftar rasa es krim
my_ice_cream_stand.display_flavors()

# (Opsional) Memanggil metode bawaan dari kelas induk (Restaurant)
print()
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()