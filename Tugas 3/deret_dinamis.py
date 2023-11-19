print('\n------PROGRAM MENAMPILKAN DERET SECARA DINAMIS------\n')

n = int(input("Masukkan nilai n: "))

# Membuat fungsi untuk menghitung faktorial
def faktorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * faktorial(n-1)

# Membuat loop untuk menampilkan deret
for i in range(n, 0, -1):
  # Mencetak nilai faktorial(i)
  print(faktorial(i), end=" ")
  # Membuat loop untuk mencetak angka dari i sampai 1
  for j in range(i, 0, -1):
    print(j, end=" ")
  # Mencetak baris baru
  print()