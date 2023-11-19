print('\n------PROGRAM MENCARI BILANGAN PRIMA TERDEKAT "N"------\n')

N = int(input("Masukkan nilai n: "))

prima_terdekat = None

# Mengulang untuk setiap bilangan dari n-1 sampai 2
for bilangan in range(N-1, 1, -1):
    # Inisialisasi variabel untuk menyimpan status prima atau tidak
    status = True

    # Mengulang untuk setiap pembagi dari 2 sampai akar bilangan
    for pembagi in range(2, int(bilangan**0.5)+1):
        # Memeriksa apakah bilangan habis dibagi pembagi
        if bilangan % pembagi == 0:
            # Jika ya, maka bilangan bukan prima dan mengubah status menjadi False
            status = False
            break

    # Jika status masih True, maka bilangan adalah prima dan disimpan sebagai prima terdekat
    if status:
        prima_terdekat = bilangan
        break

# Menampilkan prima terdekat
if prima_terdekat is None:
    print("Tidak ada bilangan prima yang lebih kecil dari", N)
else:
    print("Bilangan prima terdekat dari ", N, " yang lebih kecil adalah ", prima_terdekat)