print('\n------MENYATAKAN KALIMAT PALINDROM ATAU BUKAN------\n')

string = input("Masukkan string: ")
kata = input("Masukkan kata: ")

string = string.lower()
kata = kata.lower()

daftar_kata = string.split()
frekuensi = daftar_kata.count(kata)

print("Kata", kata, "ada", frekuensi, "buah")
