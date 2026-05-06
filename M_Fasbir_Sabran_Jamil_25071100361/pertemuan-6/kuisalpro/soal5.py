class Film:
    def __init__(self, judul, harga):
        self.judul = judul
        self.harga = harga

    def tampilkan(self):
        print(f"{self.judul} - Rp{self.harga}")

class Transaksi:
    def __init__(self):
        self.total = 0

    def tambah(self, film, jumlah):
        subtotal = film.harga * jumlah
        self.total += subtotal

    def struk(self):
        print(f"Total Pembelian: Rp{self.total}")

f1 = Film("Danur", 50000)
f2 = Film("Inside Out 2", 45000)
f3 = Film("Spiderman", 55000)

katalog = [f1, f2, f3]

