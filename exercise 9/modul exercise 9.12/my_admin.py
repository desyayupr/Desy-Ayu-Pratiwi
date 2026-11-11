from admin import Admin

# Membuat instance Admin baru
admin_user = Admin("Siti", "Aminah", "admin_siti", "siti.admin@email.com", "Bandung")

# Menguji apakah semua modul terhubung dan berfungsi dengan benar
admin_user.describe_user()
admin_user.privileges.show_privileges()