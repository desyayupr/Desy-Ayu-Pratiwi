class Restaurant:
    """A model for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name, cuisine_type, and number_served attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Atribut baru dengan nilai default 0

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")
        print(f"Jumlah pelanggan dilayani: {self.number_served}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} saat ini sedang buka!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Increment the number of customers who've been served."""
        self.number_served += additional_customers


# 1. Membuat instance bernama restaurant[cite: 4]
restaurant = Restaurant("Padang Merdeka", "Masakan Padang")

# 2. Mencetak jumlah pelanggan awal[cite: 4]
print(f"Pelanggan awal: {restaurant.number_served}")

# 3. Mengubah nilai atribut secara langsung dan mencetaknya lagi[cite: 4]
restaurant.number_served = 15
print(f"Pelanggan setelah diubah langsung: {restaurant.number_served}")

# 4. Menggunakan metode set_number_served() untuk mengatur nilai baru
restaurant.set_number_served(50)
print(f"Pelanggan setelah pakai set_number_served(): {restaurant.number_served}")

# 5. Menggunakan metode increment_number_served() untuk menambah jumlah pelanggan
restaurant.increment_number_served(25)
print(f"Total pelanggan setelah ditambah (increment): {restaurant.number_served}")