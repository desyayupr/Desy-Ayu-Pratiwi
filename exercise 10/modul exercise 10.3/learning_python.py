# pembaruan untuk file learning_python.py
filename = "learning_python.txt"

print("--- Membaca seluruh isi file sekaligus ---")
with open(filename) as file_object:
    print(file_object.read().strip())

print("\n" + "=" * 40 + "\n")

print("--- Membaca baris demi baris langsung dengan splitlines() ---")
with open(filename) as file_object:
    for line in file_object.read().splitlines():
        print(line)