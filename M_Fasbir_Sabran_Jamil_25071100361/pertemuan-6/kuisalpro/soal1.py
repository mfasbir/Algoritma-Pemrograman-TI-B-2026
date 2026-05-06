daftar_film = [
    ["Danur", 50000],
    ["Inside Out 2", 45000],
    ["Spiderman", 55000],
    ["Batman", 60000],
    ["The Nun", 48000]
]

print("--- Daftar Film CineMaju ---")
for i in range(len(daftar_film)):
    print(f"{i+1}. {daftar_film[i][0]} - Rp{daftar_film[i][1]}")

pilihan = int(input("Pilih nomor film: "))

if 1 <= pilihan <= len(daftar_film):
    film_terpilih = daftar_film[pilihan-1]
    print(f"Anda memilih: {film_terpilih[0]}")
    print(f"Harga tiket: Rp{film_terpilih[1]}")
else:
    print("Error: Nomor film tidak valid!")

