print('\n------PROGRAM MENGHAPUS SPASI BERLEBIH------\n')


# Fungsi untuk menghapus spasi berlebih pada sebuah string
def hapus_spasi(string):
  # Ubah string menjadi daftar kata-kata
  daftar_kata = string.split()
  # Gabungkan daftar kata-kata menjadi sebuah string baru dengan spasi tunggal
  string_baru = " ".join(daftar_kata)
  # Kembalikan string baru
  return string_baru

# Contoh penggunaan fungsi hapus_spasi
string = "saya tidak suka memancing ikan "
string_baru = hapus_spasi(string)
print(string_baru)
