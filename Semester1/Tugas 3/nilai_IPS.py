print('\n------PROGRAM MENGHITUNG NILAI INDEKS PRESTASI SEMESTER (IPS)------\n')

# Membuat sebuah dictionary yang berisi bobot nilai untuk setiap huruf
bobot_nilai = {"A": 4, "B": 3, "C": 2, "D": 1}

# Membaca input jumlah mata kuliah dari pengguna
jumlah_mk = int(input("Masukkan jumlah total mata kuliah: "))

# Membuat variabel untuk menyimpan total nilai dan total sks
total_nilai = 0
total_sks = 0

# Membuat loop untuk meminta input nilai dan sks untuk setiap mata kuliah
for i in range(1, jumlah_mk + 1):
  # Membaca input nilai dan sks dari pengguna
  nilai = input(f"Masukkan nilai mata kuliah ke-{i} (A/B/C/D): ")
  sks = int(input(f"Masukkan jumlah sks mata kuliah ke-{i}: "))
  # Menghitung nilai yang didapat dari mata kuliah tersebut
  nilai_mk = bobot_nilai[nilai] * sks
  # Menambahkan nilai dan sks ke total
  total_nilai += nilai_mk
  total_sks += sks

# Menghitung nilai IPS dengan membagi total nilai dengan total sks
IPS = total_nilai / total_sks

# Mencetak nilai IPS yang didapat
print(f"\n\nNilai IPS Anda adalah: {IPS:.2f}\n")
