# 1. Membuat dictionary kosong untuk menampung hasil polling
responses = {}

# 2. Menggunakan variabel penanda (flag) untuk mengontrol perulangan while
polling_active = True

while polling_active:
    # Meminta nama pengguna
    name = input("\nSiapa nama Anda? ")
    
    # Meminta destinasi liburan impian
    destination = input("If you could visit one place in the world, where would you go? ")
    
    # Menyimpan jawaban ke dalam dictionary (key: nama, value: destinasi)
    responses[name] = destination
    
    # Menanyakan apakah ada responden lain yang ingin ikut mengisi
    repeat = input("Apakah ada orang lain yang ingin mengikuti polling? (ketik 'no' untuk berhenti): ")
    if repeat.lower() == 'no':
        polling_active = False

# 3. Mencetak hasil rekapitulasi polling di akhir program
print("\n--- HASIL POLLING LIBURAN IMPIAN ---")
for name, place in responses.items():
    print(f"{name.title()} ingin sekali berkunjung ke {place.title()}.")