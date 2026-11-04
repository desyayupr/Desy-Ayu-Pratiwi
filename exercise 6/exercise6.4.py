# Membuat dictionary glossary dengan 5 istilah awal dan ditambah 5 istilah baru
glossary = {
    'dictionary': 'Struktur data di Python yang menyimpan informasi dalam bentuk pasangan kunci dan nilai (key-value pairs).',
    'list': 'Kumpulan item yang disusun berurutan dan dapat diubah (mutable), menggunakan indeks angka.',
    'loop': 'Blok kode yang digunakan untuk melakukan perulangan eksekusi secara otomatis.',
    'if-elif-else': 'Struktur percabangan kondisi untuk menguji beberapa skenario logika yang berbeda.',
    'string': 'Tipe data teks yang diapit oleh tanda kutip tunggal atau ganda.',
    # Menambahkan 5 istilah baru sesuai instruksi soal
    'integer': 'Tipe data angka bulat tanpa komponen desimal.',
    'float': 'Tipe data angka yang memiliki titik desimal.',
    'boolean': 'Tipe data yang hanya bernilai benar (True) atau salah (False).',
    'tuple': 'Kumpulan item yang disusun berurutan tetapi bersifat tetap (immutable/tidak bisa diubah).',
    'comment': 'Catatan di dalam kode program yang diawali tanda pagar (#) dan diabaikan oleh Python.'
}

# Menggunakan perulangan for dengan .items() untuk mencetak semua kata dan artinya secara otomatis
for word, meaning in glossary.items():
    print(f"{word.title()}:\n{meaning}\n")
    
# .items(): perintah digunakan dalam loop for untuk mengambil pasangan kunci dan nilai secara bersamaan dari dalam dictionary