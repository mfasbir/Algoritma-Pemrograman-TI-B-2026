hari = int(input("Masukkan jumlah hari: "))
film_count = int(input("Masukkan jumlah film: "))

matriks = []

for i in range(hari):
    baris = []
    print(f"Data Hari ke-{i+1}:")
    for j in range(film_count):
        terjual = int(input(f"  Tiket Film ke-{j+1} terjual: "))
        baris.append(terjual)
    matriks.append(baris)

print("\n--- Matriks Penjualan ---")
for baris in matriks:
    print(baris)

for i in range(hari):
    print(f"Total terjual Hari ke-{i+1}: {sum(matriks[i])}")

