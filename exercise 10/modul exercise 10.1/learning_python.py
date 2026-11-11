filename = "learning_python.txt"

# 1. Membaca seluruh file sekaligus
print("--- Membaca seluruh isi file sekaligus ---")
with open(filename) as file_object:
    contents = file_object.read()
print(contents.strip())

print("\n" + "=" * 40 + "\n")

# 2. Menyimpan baris-baris ke dalam list dan melakukan looping
print("--- Membaca dengan menyimpan ke dalam list & looping ---")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())