# 1. Mendefinisikan fungsi dengan parameter country yang memiliki nilai default 'Iceland'
def describe_city(city, country='Iceland'):
    """Menampilkan kalimat sederhana tentang letak suatu kota."""
    print(f"{city.title()} is in {country.title()}.")

# 2. Pemanggilan pertama: Menggunakan kota di negara default (tanpa argumen country)
describe_city('reykjavik')

# 3. Pemanggilan kedua: Kota lain yang juga di Iceland
describe_city('akureyri')

# 4. Pemanggilan ketiga: Kota yang berada di negara lain (bukan di negara default)
describe_city('tokyo', 'japan')