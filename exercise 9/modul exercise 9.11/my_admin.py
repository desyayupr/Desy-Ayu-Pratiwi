from admin_modul import Admin

# Membuat instance Admin baru[cite: 13]
admin_user = Admin("Budi", "Santoso", "admin_budi", "budi.admin@email.com", "Surakarta")

# Menampilkan informasi profil dan daftar hak akses[cite: 13]
admin_user.describe_user()
admin_user.privileges.show_privileges()