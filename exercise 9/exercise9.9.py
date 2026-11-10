class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range_distance = 150
        elif self.battery_size == 65:
            range_distance = 225
        else:
            range_distance = 250

        print(f"Mobil ini dapat menempuh jarak sekitar {range_distance} mil dengan pengisian penuh.")

    def upgrade_battery(self):
        """Check the battery size and set the capacity to 65 if it isn't already."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai berhasil ditingkatkan (upgrade) ke 65 kWh.")
        else:
            print("Baterai sudah berkapasitas 65 kWh.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


# 1. Membuat mobil listrik dengan ukuran baterai default (40 kWh)
my_electric_car = ElectricCar('nissan', 'leaf', 2024)

print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()

# 2. Memanggil get_range() pertama kali sebelum di-upgrade
my_electric_car.battery.get_range()

# 3. Melakukan upgrade baterai, lalu memanggil get_range() kedua kalinya
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()