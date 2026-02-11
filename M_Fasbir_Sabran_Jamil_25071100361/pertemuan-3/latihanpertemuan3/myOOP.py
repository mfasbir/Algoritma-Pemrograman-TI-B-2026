# ==========================================
# A. INHERITANCE
# ==========================================

class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga}"


class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi

    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga} dengan garansi {self.garansi} tahun"


class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga} kadaluarsa {self.tanggal_kadaluarsa}"


# ==========================================
# B. POLYMORPHISM
# ==========================================

class Notifikasi:
    def kirim(self):
        return "Mengirim notifikasi umum"


class Email(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui Email"


class SMS(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui SMS"


class WhatsApp(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui WhatsApp"


class Telegram(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui Telegram"



# ==========================================
# C. ENCAPSULATION
# ==========================================

class Mahasiswa:
    def __init__(self):
        self.__nilai = 0  # atribut private

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
            return "Nilai berhasil disimpan"
        else:
            return "Nilai tidak valid"

    def get_nilai(self):
        return self.__nilai
