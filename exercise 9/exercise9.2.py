class Restaurant:
    """A model for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}\n")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} saat ini sedang buka!")


# Membuat tiga instance (objek) berbeda dari kelas Restaurant
restaurant_1 = Restaurant("Padang Merdeka", "Masakan Padang")
restaurant_2 = Restaurant("Sate Senayan", "Kuliner Nusantara")
restaurant_3 = Restaurant("Bakso Malang Karapitan", "Street Food / Bakso")

# Memanggil metode describe_restaurant() untuk masing-masing instance
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()