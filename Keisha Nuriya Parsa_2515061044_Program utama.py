import keisha044

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("=== PENJUMLAHAN MATRIKS ===")
hasil = keisha044.tambah_matriks(A, B)

for baris in hasil:
    print(baris)

print("\n=== PERKALIAN MATRIKS ===")
hasil = keisha044.kali_matriks(A, B)

for baris in hasil:
    print(baris)

print("\n=== DETERMINAN MATRIKS ===")
print(keisha044.determinan_3x3(A))