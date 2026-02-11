from myOOP import *

# ==========================================
# TEST INHERITANCE
# ==========================================

tv = ProdukElektronik("TV", "3.000.000", 2)
roti = ProdukMakanan("Roti", "15.000", "12-12-2026")

print(tv.info_produk())
print(roti.info_produk())

# ==========================================
# TEST POLYMORPHISM
# ==========================================


notif1 = Email()
notif2 = SMS()
notif3 = WhatsApp()
notif4 = Telegram()

print(notif1.kirim())
print(notif2.kirim())
print(notif3.kirim())
print(notif4.kirim())


# ==========================================
# TEST ENCAPSULATION
# ==========================================

mhs = Mahasiswa()

print(mhs.set_nilai(85))
print("Nilai:", mhs.get_nilai())

print(mhs.set_nilai(120))  # Tidak valid
