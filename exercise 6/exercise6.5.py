# 1. Membuat dictionary sungai dan negara tempat mengalirnya
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# 2. Loop untuk mencetak kalimat tentang setiap sungai dan negara
print("--- Informasi Sungai dan Negara ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 3. Loop untuk mencetak nama setiap sungai (keys)
print("\n--- Daftar Sungai ---")
for river in rivers.keys(): # atau cukup tulis 'for river in rivers:'
    print(river.title())

# 4. Loop untuk mencetak nama setiap negara (values)
print("\n--- Daftar Negara ---")
for country in rivers.values():
    print(country.title())
    
# .items(): untuk mengambil pasangan kunci dan nilai secara bersamaan di dalam perulangan.
# .keys(): digunakan jika hanya ingin mengambil bagian kuncinya saja.
# .values(): digunakan jika hanya ingin mengambil bagian nilai saja.