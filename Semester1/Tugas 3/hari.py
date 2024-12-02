print('\n------PROGRAM MENAMPILKAN JUMLAH HARI DALAM SUATU BULAN------\n')

# Membuat sebuah list yang berisi jumlah hari untuk setiap bulan
jumlah_hari = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Membaca input bulan dari pengguna
bulan = int(input("Masukkan bulan (1-12): "))

# Mengecek apakah bulan valid atau tidak
if bulan >= 1 and bulan <= 12:
  # Menampilkan jumlah hari pada bulan tersebut
  print(f"Jumlah hari: {jumlah_hari[bulan-1]}")
else:
  # Menampilkan pesan bahwa bulan tidak valid
  print("Bulan yang Anda masukkan tidak valid")