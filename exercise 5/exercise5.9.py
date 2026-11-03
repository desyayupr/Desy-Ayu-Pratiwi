# Memulai dengan list kosong (atau Anda bisa mengosongkannya menggunakan metode penghapusan seperti .clear())
usernames = []

# Menambahkan pengujian if untuk memeriksa apakah list tidak kosong
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
    
# 'if usernames': sebuah list yang memiliki isi (tidak kosong) akan bernilai True, jika dijadikan kondisi dalam pernyataan 'if'
# jika list kosong [], maka kondisi tersebut akan bernilai 'false'
