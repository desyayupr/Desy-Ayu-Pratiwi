# 1. Membuat list berisi lima atau lebih username, termasuk 'admin'
usernames = ['admin', 'jaden', 'sarah', 'eric', 'alice']

# 2. Melakukan loop pada list usernames
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
        
# for username in usernames: digunakan untuk mengambil setiap nama pengguna di dalam list satu per satu secara otomatis
