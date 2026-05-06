struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

#Soal A
def total_ukuran(folder):
    total = 0
    for item in folder.values():
        if isinstance(item, dict): 
            total += total_ukuran(item)
        else:  
            total += item
    return total

print("Total ukuran skripsi:", total_ukuran(struktur), "KB")


#Soal B
def hitung_file(folder):
    jumlah = 0
    for item in folder.values():
        if isinstance(item, dict): 
            jumlah += hitung_file(item)
        else:  
            jumlah += 1
    return jumlah

print("Jumlah file:", hitung_file(struktur), "file")

#Soal C
def cari_terbesar(folder):
    terbesar_nama = ""
    terbesar_ukuran = 0

    for nama, item in folder.items():
        if isinstance(item, dict):  
            nama_file, ukuran = cari_terbesar(item)
            if ukuran > terbesar_ukuran:
                terbesar_nama = nama_file
                terbesar_ukuran = ukuran
        else:  
            if item > terbesar_ukuran:
                terbesar_nama = nama
                terbesar_ukuran = item

    return (terbesar_nama, terbesar_ukuran)

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")

#Soal D
def tampilkan_tree(folder, nama="root", level=0):
    indent = "  " * level

    if level == 0:
        print(f"📁 {nama}")

    for key, item in folder.items():
        if isinstance(item, dict): 
            print(f"{indent}📁 {key}")
            tampilkan_tree(item, key, level + 1)
        else:  
            print(f"{indent}📄 {key} ({item} KB)")

tampilkan_tree(struktur["Skripsi_Aqil"], "Skripsi_Aqil")