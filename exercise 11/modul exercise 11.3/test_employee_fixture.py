import pytest
from employee import Employee


@pytest.fixture
def employee_instance():
    """Fixture untuk membuat instance Employee default untuk pengujian."""
    return Employee("Budi", "Santoso", 50000)


def test_give_default_raise(employee_instance):
    """Menguji kenaikan gaji default menggunakan fixture."""
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 55000


def test_give_custom_raise(employee_instance):
    """Menguji kenaikan gaji kustom menggunakan fixture."""
    employee_instance.give_raise(10000)
    # Catatan: Perlu diingat bahwa dalam Pytest, fixture bersifat independen 
    # untuk setiap fungsi test (fungsi test menerima salinan/instance baru).
    assert employee_instance.annual_salary == 60000 + 10000