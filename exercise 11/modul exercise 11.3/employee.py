class Employee:
    """Representasi seorang karyawan beserta gaji tahunannya."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Menambahkan jumlah kenaikan gaji, defaultnya adalah $5.000."""
        self.annual_salary += amount