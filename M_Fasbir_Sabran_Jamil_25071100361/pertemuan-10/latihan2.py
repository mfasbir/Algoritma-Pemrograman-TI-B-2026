# Fungsi untuk Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        kiri = arr[:mid]
        kanan = arr[mid:]

        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0

        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                arr[k] = kiri[i]
                i += 1
            else:
                arr[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            arr[k] = kiri[i]
            i += 1
            k += 1
        while j < len(kanan):
            arr[k] = kanan[j]
            j += 1
            k += 1

#Counting Sort berdasarkan digit
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Fungsi utama Radix Sort
def radix_sort(arr):
    if not arr:
        return
    maks = max(arr)
    exp = 1
    while maks // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# --- Program Utama ---
def main():
    try:
        n = int(input("Masukkan jumlah elemen: "))
        if n <= 0:
            print("Jumlah elemen harus lebih dari 0.")
            return

        data_asli = []
        for i in range(n):
            while True:
                val = int(input(f"Elemen ke-{i+1}: "))
                if val >= 0:
                    data_asli.append(val)
                    break
                else:
                    print("Input tidak valid! Masukkan bilangan non-negatif.")

        data_merge = data_asli.copy()
        data_radix = data_asli.copy()

        print("\n--- Hasil Merge Sort ---")
        print("Sebelum:", data_asli)
        merge_sort(data_merge)
        print("Sesudah:", data_merge)

        print("\n--- Hasil Radix Sort ---")
        print("Sebelum:", data_asli)
        radix_sort(data_radix)
        print("Sesudah:", data_radix)

    except ValueError:
        print("Error: Harap masukkan angka bulat yang valid.")

if __name__ == "__main__":
    main()

    
