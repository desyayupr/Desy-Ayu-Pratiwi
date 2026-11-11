from employee import Employee


def test_give_default_raise():
    """Menguji kenaikan gaji default sebesar $5.000."""
    emp = Employee("Budi", "Santoso", 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000


def test_give_custom_raise():
    """Menguji kenaikan gaji dengan jumlah kustom (misal: $10.000)."""
    emp = Employee("Siti", "Rahma", 60000)
    emp.give_raise(10000)
    assert emp.annual_salary == 70000