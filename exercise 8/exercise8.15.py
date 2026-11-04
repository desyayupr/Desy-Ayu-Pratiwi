# pada latihan ini perlu membuat dua buah file yang diletakkan dalam folder yang sama

# file pertama
# File: printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    Mensimulasikan pencetakan setiap desain, sampai habis.
    Memindahkan setiap desain ke completed_models setelah dicetak.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang telah dicetak."""
    print("\nModel berikut telah dicetak:")
    for completed_model in completed_models:
        print(completed_model)

# file kedua
# File: printing_models.py

import printing_functions # untuk memanggil file modul printing_functions

# Menyiapkan data awal
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Memanggil fungsi menggunakan nama modul (module_name.function_name)
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)