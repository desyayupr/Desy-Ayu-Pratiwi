# 1. Mendefinisikan class Restaurant
class Restaurant:
    """Model sederhana dari sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut restaurant_name dan cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak informasi deskripsi restoran."""
        print(f"Nama Restoran: {self.restaurant_name.title()}")
        print(f"Jenis Masakan: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name.title()} sekarang sedang buka!\n")


# 2. Membuat instance (objek) bernama restaurant
restaurant = Restaurant('sederhana', 'masakan padang')

# 3. Mencetak kedua atribut secara individual
print("--- Mengakses Atribut Secara Terpisah ---")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print("\n--- Memanggil Metode pada Class ---")
# 4. Memanggil kedua metode
restaurant.describe_restaurant()
restaurant.open_restaurant()

# calss : untuk mendefinisikan cetak biru (blueprint) atau kelas baru bernama restaurant/sebagai templat untuk membuat suatu objek
# metode inisialisasi:
# 1. __init__ : disebut sebagai konstruktor, utk menginialisasi (memberikan nilai awal) pada sebuah obejk saat objek pertama kali dibuat dari class
# 2. describe_restaurant(self): mencetak informasi ringkas (deskripsi) mengenai restoran ke layar.
# 3. open_restaurant(self): mencetak pesan status operasional yang menyatakan bahwa restoran tersebut sedang dalam keadaan buka.