# Perulangan while True ini tidak memiliki kondisi berhenti (tanpa break)
# Sehingga teks di bawah akan tercetak terus-menerus tanpa henti ke layar terminal
x = 1
while True:
    print(f"Angka saat ini: {x} (Perulangan tanpa batas aktif!)")
    x += 1

# cara memberhentikan : tekan ctrl + c secara bersamaan