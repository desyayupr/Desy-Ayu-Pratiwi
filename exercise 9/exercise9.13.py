from random import randint

class Die:
    """A class representing a physical die."""

    def __init__(self, sides=6):
        """Initialize the die with a default of 6 sides."""
        self.sides = sides  # Atribut jumlah sisi dadu dengan default 6

    def roll_die(self):
        """Print a random number between 1 and the number of sides the die has."""
        x = randint(1, self.sides)
        print(x)


# 1. Membuat dadu standar (6 sisi) dan melemparnya 10 kali
print("--- Pelemparan Dadu 6 Sisi (10 kali) ---")
d6 = Die()
for _ in range(10):
    d6.roll_die()

# 2. Membuat dadu berukuran 10 sisi dan melemparnya 10 kali
print("\n--- Pelemparan Dadu 10 Sisi (10 kali) ---")
d10 = Die(10)
for _ in range(10):
    d10.roll_die()

# 3. Membuat dadu berukuran 20 sisi dan melemparnya 10 kali
print("\n--- Pelemparan Dadu 20 Sisi (10 kali) ---")
d20 = Die(20)
for _ in range(10):
    d20.roll_die()