def bubble_sort(arr):
    n = len(arr)
    data = arr.copy() 
    total_swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                total_swaps += 1
                swapped = True

        if not swapped:
            break
            
    return data, total_swaps

def selection_sort(arr):
    n = len(arr)
    data = arr.copy() 
    total_swaps = 0
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if data[j] > data[max_idx]:
                max_idx = j

        if max_idx != i:
            data[i], data[max_idx] = data[max_idx], data[i]
            total_swaps += 1
            
    return data, total_swaps

data = [918, 336, 637, 814, 507, 685, 854, 933, 970, 461, 26, 884, 684, 47, 922, 246, 431, 985, 412, 679, 708, 354, 369, 396, 406, 882, 119, 682, 378, 578, 208, 899, 344, 436, 153, 835, 836, 985, 117, 619, 225, 345, 210, 606, 313, 998, 681, 989, 212, 163, 762, 389, 906, 423, 204, 627, 430, 568, 430, 71, 429, 492, 817, 577, 621, 914, 500, 783, 872, 992, 498, 477, 34, 570, 113, 2, 58, 844, 464, 293, 302, 183, 711, 777, 71, 441, 261, 713, 544, 528, 759, 193, 163, 272, 389, 979, 608, 977, 721, 508, 619, 875, 948, 750, 991, 711, 855, 111, 555, 608, 535, 603, 538, 753, 190, 441, 85, 200, 193, 577, 774, 578, 405, 306, 256, 926, 433, 444, 459, 368, 187, 671, 701, 714, 411, 940, 603, 736, 665, 947, 517, 19, 365, 165, 514, 133, 491, 642, 636, 957]

sorted_bubble, swaps_bubble = bubble_sort(data)
print("Bubble Sort (kecil → besar):", sorted_bubble)
print("Jumlah swap Bubble Sort:", swaps_bubble)

print("-" * 30)

sorted_selection, swaps_selection = selection_sort(data)
print("Selection Sort (besar → kecil):", sorted_selection)
print("Jumlah swap Selection Sort:", swaps_selection)