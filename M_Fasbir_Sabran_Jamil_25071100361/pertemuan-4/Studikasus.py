print("=== Program Login ATM ===")

username_benar = "fasbir"
pin_benar = 1234

kesempatan = 3

while kesempatan > 0:
    username = input("Masukkan username: ")
    
    try:
        pin = int(input("Masukkan PIN (angka): "))
        
        if username == username_benar and pin == pin_benar:
            print("Login berhasil!")
            break
        else:
            kesempatan -= 1
            print("Username atau PIN salah!")
            print("Sisa kesempatan:", kesempatan)
    
    except ValueError:
        print("PIN harus berupa angka!")
        kesempatan -= 1
        print("Sisa kesempatan:", kesempatan)

if kesempatan == 0:
    print("Akun diblokir karena terlalu banyak kesalahan.")