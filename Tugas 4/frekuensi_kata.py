print('\n------PROGRAM MENAMPILKAN FREKUENSI SUATU KATA------\n')

# Fungsi untuk menghitung frekuensi kemunculan suatu kata dalam sebuah string
def hitung_frekuensi(kata, string):
  # Ubah kata dan string menjadi huruf-huruf kecil
  kata = kata.lower()
  string = string.lower()
  # Pisahkan string menjadi daftar kata-kata
  daftar_kata = string.split()
  # Hitung berapa kali kata muncul dalam daftar kata
  frekuensi = daftar_kata.count(kata)
  # Kembalikan nilai frekuensi
  return frekuensi

# Contoh penggunaan fungsi hitung_frekuensi
string = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata = "makan"
frekuensi = hitung_frekuensi(kata, string)
print(kata, "ada", frekuensi, "buah")
