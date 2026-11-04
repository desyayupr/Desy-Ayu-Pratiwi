# 1. Mendefinisikan fungsi dengan parameter wajib dan **car_info
def make_car(manufacturer, model, **car_info):
    """Menyimpan informasi tentang mobil ke dalam dictionary."""
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()
    return car_info

# 2. Memanggil fungsi sesuai format instruksi
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# 3. Mencetak dictionary yang dihasilkan
print("--- INFORMASI MOBIL ---")
print(car)