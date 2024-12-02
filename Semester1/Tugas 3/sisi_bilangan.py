print('\n------PROGRAM MENAMPILKAN SISI SEGITIGA------\n')

# Membaca input sisi 1 dari pengguna
try:
  sisi1 = int(input("Masukkan sisi 1: "))
except ValueError:
  print("Input yang Anda masukkan tidak valid")
  exit()

# Membaca input sisi 2 dari pengguna
try:
  sisi2 = int(input("Masukkan sisi 2: "))
except ValueError:
  print("Input yang Anda masukkan tidak valid")
  exit()

# Membaca input sisi 3 dari pengguna
try:
  sisi3 = int(input("Masukkan sisi 3: "))
except ValueError:
  print("Input yang Anda masukkan tidak valid")
  exit()

# Mengecek kondisi sisi-sisi segitiga
if sisi1 == sisi2 == sisi3:
  # Mencetak pesan bahwa 3 sisi sama
  print("3 sisi sama")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
  # Mencetak pesan bahwa 2 sisi sama
  print("2 sisi sama")
else:
  # Mencetak pesan bahwa tidak ada yang sama
  print("Tidak ada yang sama")
