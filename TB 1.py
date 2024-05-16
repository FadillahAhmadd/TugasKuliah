import itertools
import re

# Membuka file dan membaca semua baris
with open('Matrix.txt', 'r') as file:
    # Membaca dua baris pertama dan membaginya menjadi dua angka terpisah
    # Dimensi matriks
    dimensi = file.readline().strip().split()
    baris = int(dimensi[0])  # Jumlah baris
    kolom = int(dimensi[1])  # Jumlah kolom

    matriks = []

    # Membaca elemen-elemen matriks
    for _ in range(baris):
        # Membaca satu baris elemen matriks
        elemen_matriks = file.readline().strip()
        matriks.append(elemen_matriks)

    # Menggabungkan elemen matriks menjadi satu string
    string_terkode = "".join(char for grup in itertools.zip_longest(*matriks, fillvalue='') for char in grup)

    # Menggunakan regex untuk mengganti pola tertentu dengan spasi
    # Mendekodekan string yang telah dienkripsi
    pola = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
    string_terdekripsi = re.sub(pola, ' ', string_terkode)

    # Menampilkan string hasil dekripsi
    print(string_terdekripsi)
