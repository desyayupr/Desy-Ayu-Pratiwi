from city_functions import city_country

def test_city_country():
    """Memverifikasi format City, Country standar."""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

def test_city_country_population():
    """Memverifikasi format City, Country dengan tambahan populasi."""
    santiago_chile = city_country('santiago', 'chile', population=5000000)
    assert santiago_chile == 'Santiago, Chile - population 5000000'