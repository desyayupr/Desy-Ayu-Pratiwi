# file pertama
# File: car_module.py

def make_car(manufacturer, model, **car_info):
    """Menyimpan informasi tentang mobil ke dalam dictionary."""
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()
    return car_info

# file kedua
# File: my_cars.py

# --- Pendekatan 1: import module_name ---
import car_module

car1 = car_module.make_car('subaru', 'outback', color='blue')
print("Pendekatan 1:", car1)


# --- Pendekatan 2: from module_name import function_name ---
from car_module import make_car

car2 = make_car('toyota', 'avanza', color='silver')
print("Pendekatan 2:", car2)


# --- Pendekatan 3: from module_name import function_name as fn ---
from car_module import make_car as mc

car3 = mc('honda', 'civic', color='black')
print("Pendekatan 3:", car3)


# --- Pendekatan 4: import module_name as mn ---
import car_module as cm

car4 = cm.make_car('tesla', 'model 3', color='white')
print("Pendekatan 4:", car4)


# --- Pendekatan 5: from module_name import * (Import semua fungsi) ---
from car_module import *

car5 = make_car('suzuki', 'ertiga', color='grey')
print("Pendekatan 5:", car5)

# noted: tempatkan file pertama dan file kedua dalam sebuah file terpisah