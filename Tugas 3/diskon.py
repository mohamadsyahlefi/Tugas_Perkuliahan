print('\n------PROGRAM MENAMPILKAN DISKON BELANJA------\n')

# Membaca input harga pembelian dari pengguna
harga = int(input("Masukkan harga pembelian: "))

# Membuat variabel untuk menyimpan harga setelah diskon
harga_diskon = harga

# Mengecek apakah harga pembelian lebih dari 1.500.000
if harga > 1500000:
  # Menghitung harga setelah diskon 10%
  harga_diskon = harga * 0.9
  # Mencetak pesan bahwa pembeli mendapatkan diskon
  print("Anda mendapatkan diskon 10%")

# Mencetak harga yang harus dibayar
print(f"Harga yang harus dibayar: {harga_diskon}")
