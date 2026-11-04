# 1. Mendefinisikan fungsi menggunakan kata kunci 'return'
def city_country(city, country):
    """Mengembalikan string berformat 'City, Country'."""
    formatted_name = f"{city.title()}, {country.title()}"
    return formatted_name

# 2. Memanggil fungsi dengan tiga pasangan kota-negara berbeda dan mencetak hasilnya
city1 = city_country('santiago', 'chile')
city2 = city_country('tokyo', 'japan')
city3 = city_country('jakarta', 'indonesia')

print(city1)
print(city2)
print(city3)

# return: bertugas mengirimkan hasil akhir dari dalam fungsi kembali ke baris kode yang memanggilnya