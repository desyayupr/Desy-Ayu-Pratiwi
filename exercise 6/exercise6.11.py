# 1. Membuat dictionary utama 'cities' yang berisi dictionary untuk masing-masing kota
cities = {
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'fact': 'merupakan salah satu wilayah metropolitan paling padat dan maju di dunia.',
    },
    'paris': {
        'country': 'perancis',
        'population': '2,1 juta jiwa',
        'fact': 'dikenal sebagai Kota Cinta dan rumah bagi Menara Eiffel.',
    },
    'surakarta': {
        'country': 'indonesia',
        'population': '522 ribu jiwa',
        'fact': 'terkenal dengan kekayaan budaya Jawa serta sebutan kota Solo.',
    }
}

# 2. Melakukan perulangan untuk mengakses nama kota (key) dan informasi detailnya (value berupa dictionary)
for city_name, city_info in cities.items():
    print(f"\nKota: {city_name.title()}")
    
    # Mengambil data dari dictionary di dalam value
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    
    print(f"- Negara    : {country.title()}")
    print(f"- Populasi  : {population}")
    print(f"- Fakta Unik: {fact}")