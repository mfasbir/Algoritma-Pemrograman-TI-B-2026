daftar_film = [
    ["Danur", 50000],
    ["Inside Out 2", 45000],
    ["Spiderman", 55000],
    ["Batman", 60000],
    ["The Nun", 48000]
]

keranjang = []
total_seluruh = 0

while True:
    print("\n(Masukkan 0 untuk selesai)")
    pilihan = int(input("Pilih nomor film: "))
    
    if pilihan == 0:
        break
    
    if 1 <= pilihan <= len(daftar_film):
        jumlah = int(input("Jumlah tiket: "))
        film = daftar_film[pilihan-1]
        
        keranjang.append([film[0], jumlah, film[1] * jumlah])
        total_seluruh += film[1] * jumlah
    else:
        print("Nomor tidak valid!")

print("\n--- Daftar Pembelian ---")
for item in keranjang:
    print(f"{item[0]} x{item[1]} = Rp{item[2]}")

print(f"TOTAL HARGA: Rp{total_seluruh}")