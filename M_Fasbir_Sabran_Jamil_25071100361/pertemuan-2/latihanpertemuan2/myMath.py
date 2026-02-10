
def penambahan(a, b):
  return a + b

def pengurangan(a, b):
  return a - b

def perkalian(a, b):
  return a * b

def pembagian(a, b):
  if b == 0:
    return "Pembagian tidak dapat dilakukan karena pembagi bernilai 0"
  else:
    return a / b

def modulus(a, b):
  return a % b

def fibonacci(n):
  hasil = []
  a, b = 0, 1
  for i in range(n):
    hasil.append(a)
    a, b = b, a + b
  return hasil