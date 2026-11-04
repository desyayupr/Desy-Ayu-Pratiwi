# 1. Memperluas dictionary cities dengan menambahkan kunci baru (currency dan landmark)
cities = {
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'currency': 'Yen (JPY)',
        'landmark': 'Tokyo Tower & Shibuya Crossing',
        'fact': 'merupakan salah satu wilayah metropolitan paling padat dan maju di dunia.',
    },
    'paris': {
        'country': 'perancis',
        'population': '2,1 juta jiwa',
        'currency': 'Euro (EUR)',
        'landmark': 'Menara Eiffel & Museum Louvre',
        'fact': 'dikenal sebagai Kota Cinta dan pusat mode dunia.',
    },
    'surakarta': {
        'country': 'indonesia',
        'population': '522 ribu jiwa',
        'currency': 'Rupiah (IDR)',
        'landmark': 'Keraton Surakarta & Pura Mangkunegaran',
        'fact': 'terkenal dengan kekayaan budaya Jawa serta julukan Kota Solo.',
    }
}

# 2. Memperbaiki dan mempercantik formatting output (membangun tampilan direktori yang rapi)
print("=" * 50)
print("       DIREKTORI PROFIL KOTA DUNIA (EDISI 6-12)       ")
print("=" * 50)

# Melakukan perulangan untuk mengekstrak data bersarang (dictionary di dalam dictionary)
for city_name, info in cities.items():
    # Format judul kota dengan huruf kapital di setiap kata dan dekorasi garis tepi
    print(f"\n🌍 KOTA: {city_name.upper()}")
    print("-" * 40)
    print(f"  • Negara         : {info['country'].title()}")
    print(f"  • Populasi       : {info['population']}")
    print(f"  • Mata Uang      : {info['currency']}")
    print(f"  • Landmark Utama : {info['landmark']}")
    print(f"  • Fakta Unik     : {info['fact']}")

print("\n" + "=" * 50)
print("           PROGRAM SELESAI DIJALANKAN          ")
print("=" * 50)