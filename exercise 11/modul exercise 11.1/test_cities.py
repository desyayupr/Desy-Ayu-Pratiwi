from city_functions import city_country

def test_city_country():
    """Memverifikasi apakah fungsi city_country() dapat mengembalikan format yang benar."""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'