# Fungsi Linear Search
def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

# Fungsi Binary Search
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

# Data
data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]

print("Data saat ini:", data)
x = int(input("Masukkan nilai yang dicari: "))

result_linear = linearSearch(data, x)
print("\n[Linear Search]")
if result_linear != -1:
  print("Ada di index", result_linear)
else:
  print(result_linear)

data.sort() 
print("\n[Binary Search - Data Diurutkan]")
print("Data sorted:", data)

result_binary = binarySearch(data, x)
if result_binary != -1:
  print("Ada di index", result_binary)
else:
  print(result_binary)