# === BAGIAN A ===

def tebak_angka(angka_rahasia, maks_percobaan):
    """Menjalankan logika perulangan tebakan hingga benar atau percobaan habis."""
    percobaan = 0
    while percobaan < maks_percobaan:
        tebakan = int(input(f"Percobaan {percobaan + 1}/{maks_percobaan} - Masukkan tebakan: "))
        percobaan += 1
        
        if tebakan < angka_rahasia:
            print("Terlalu kecil")
        elif tebakan > angka_rahasia:
            print("Terlalu besar")
        else:
            print("Benar!")
            return True, maks_percobaan - percobaan
            
    print(f"Maaf, percobaan habis. Angka rahasianya adalah {angka_rahasia}.")
    return False, 0

def hitung_skor(berhasil, sisa_percobaan):
    """Menghitung skor berdasarkan status keberhasilan dan sisa percobaan."""
    if berhasil:
        return sisa_percobaan * 10
    return 0

def main_satu_ronde(nama, nomor_ronde):
    """Mengambil angka rahasia dan mengembalikan hasil satu ronde [nama, skor]."""
    DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
    
    print(f"\n--- Ronde {nomor_ronde + 1} ---")
    berhasil, sisa = tebak_angka(angka_rahasia, 7)
    skor = hitung_skor(berhasil, sisa)
    
    return [nama, skor]




# === BAGIAN B ===

def tampilkan_riwayat(riwayat):
    """Menampilkan daftar riwayat permainan dalam bentuk tabel sederhana."""
    if not riwayat:
        print("Belum ada riwayat.")
        return

    print("\nRIWAYAT PERMAINAN")
    print("-" * 30)
    print(f"{'No':<4} | {'Nama':<15} | {'Skor':<5}")
    print("-" * 30)
    for i in range(len(riwayat)):
        print(f"{i + 1:<4} | {riwayat[i][0]:<15} | {riwayat[i][1]:<5}")


# === BAGIAN C ===

def selection_sort_riwayat(riwayat):
    """Mengurutkan salinan riwayat dari skor tertinggi ke terendah."""
    data = []
    for item in riwayat:
        data.append([item[0], item[1]])



def tampilkan_leaderboard(riwayat):
    """Menampilkan urutan peringkat pemain berdasarkan skor tertinggi."""
    if not riwayat:
        return






# === PROGRAM UTAMA ===

def main():
    riwayat_global = []
    nomor_ronde = 0
    
    print("Selamat Datang di Game Higher or Lower!")
    nama_pemain = input("Masukkan nama Anda: ")
    
    main_lagi = "y"
    while main_lagi.lower() == "y":
        hasil_ronde = main_satu_ronde(nama_pemain, nomor_ronde)
        riwayat_global.append(hasil_ronde)
        
        nomor_ronde += 1
        main_lagi = input("\nIngin bermain lagi? (y/n): ")
    
    tampilkan_riwayat(riwayat_global)
    tampilkan_leaderboard(riwayat_global)
    print("\nTerima kasih telah bermain!")

if __name__ == "__main__":
    main()