print('\n------PROGRAM MENAMPILKAN KATA TERPENDEK & TERPANJANG DARI SUATU KALIMAT------\n')

# Fungsi untuk menemukan kata terpendek dan terpanjang dalam sebuah kalimat
def cari_kata(kalimat):
  # Ubah kalimat menjadi daftar kata-kata
  daftar_kata = kalimat.split()
  # Inisialisasi variabel untuk menyimpan kata terpendek dan terpanjang
  kata_terpendek = daftar_kata[0]
  kata_terpanjang = daftar_kata[0]
  # Looping untuk setiap kata dalam daftar kata
  for kata in daftar_kata:
    # Jika panjang kata lebih kecil dari panjang kata terpendek, maka update kata terpendek
    if len(kata) < len(kata_terpendek):
      kata_terpendek = kata
    # Jika panjang kata lebih besar dari panjang kata terpanjang, maka update kata terpanjang
    if len(kata) > len(kata_terpanjang):
      kata_terpanjang = kata
  # Kembalikan nilai kata terpendek dan terpanjang
  return kata_terpendek, kata_terpanjang

# Contoh penggunaan fungsi cari_kata
kalimat = "red snakes and a black frog in the pool"
kata_terpendek, kata_terpanjang = cari_kata(kalimat)
print("terpendek:", kata_terpendek, ", terpanjang:", kata_terpanjang)
