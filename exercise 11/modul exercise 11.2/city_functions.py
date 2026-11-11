def city_country(city, country, population=''):
    """Menggabungkan nama kota, negara, dan populasi (opsional)."""
    if population:
        formatted_location = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_location = f"{city.title()}, {country.title()}"
    return formatted_location