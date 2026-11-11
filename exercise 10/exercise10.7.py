print("--- Kalkulator Penjumlahan Berkelanjutan ---")
print("(Ketik 'q' atau 'quit' kapan saja untuk keluar dari program)\n")

while True:
    # Meminta input angka pertama
    first_number = input("Masukkan angka pertama: ")
    if first_number.lower() in ['q', 'quit']:
        print("Terima kasih! Program dihentikan.")
        break
        
    try:
        num1 = int(first_number)
    except ValueError:
        print("-> Peringatan: Masukan bukan berupa angka yang valid. Silakan coba lagi.\n")
        continue

    # Meminta input angka kedua
    second_number = input("Masukkan angka kedua: ")
    if second_number.lower() in ['q', 'quit']:
        print("Terima kasih! Program dihentikan.")
        break
        
    try:
        num2 = int(second_number)
    except ValueError:
        print("-> Peringatan: Masukan bukan berupa angka yang valid. Silakan coba lagi.\n")
        continue

    # Melakukan penjumlahan jika kedua input valid
    result = num1 + num2
    print(f"Hasil penjumlahan dari {num1} + {num2} adalah: {result}\n")