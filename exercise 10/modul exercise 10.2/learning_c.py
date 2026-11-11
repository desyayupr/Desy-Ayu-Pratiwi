filename = "learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    # Ganti kata 'Python' dengan 'C', lalu hilangkan spasi/newline berlebih di ujung baris
    modified_line = line.replace('Python', 'C')
    print(modified_line.strip())