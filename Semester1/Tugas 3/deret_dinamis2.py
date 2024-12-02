print('\n------PROGRAM MENAMPILKAN DERET SECARA DINAMIS SESUAI INPUT------\n')

tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

# Membuat variabel untuk menyimpan nilai saat ini
nilai = 1

# Membuat loop untuk menampilkan deret
for i in range(tinggi):
  # Membuat loop untuk mencetak nilai sebanyak lebar
  for j in range(lebar):
    # Mencetak nilai dengan format rata kanan
    print(f"{nilai:>2}", end=" ")
    # Menambahkan nilai dengan 1
    nilai += 1
  # Mencetak baris baru
  print()