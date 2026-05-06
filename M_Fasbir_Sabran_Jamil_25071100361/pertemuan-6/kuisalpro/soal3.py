total_bayar = 300000

while True:
    uang_masuk = int(input(f"Total tagihan Rp{total_bayar}. Masukkan uang Anda: "))
    
    if uang_masuk >= total_bayar:
        break
    else:
        print("Uang kurang! Silakan masukkan jumlah yang tepat.")

kembalian = uang_masuk - total_bayar

print("\n--- Ringkasan Transaksi ---")
print(f"Total: Rp{total_bayar}")
print(f"Dibayar: Rp{uang_masuk}")

if kembalian == 0:
    print("Uang pas, tidak ada kembalian.")
else:
    print(f"Kembalian Anda: Rp{kembalian}")