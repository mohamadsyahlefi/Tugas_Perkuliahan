print('\n------PROGRAM MENAMPILKAN DERET BILANGAN PRIMA------\n')

N = int(input("Masukkan nilai N: "))

# Inisialisasi variabel untuk menyimpan bilangan prima
prima = []

# Inisialisasi variabel untuk menyimpan bilangan yang akan dicek
bilangan = 2

# Mengulang selama bilangan kurang dari atau sama dengan N
while bilangan <= N:
    # Inisialisasi variabel untuk menyimpan status prima atau tidak
    status = True

    # Mengulang untuk setiap pembagi dari 2 sampai akar bilangan
    pembagi = 2
    while pembagi * pembagi <= bilangan:
        # Memeriksa apakah bilangan habis dibagi pembagi
        if bilangan % pembagi == 0:
            # Jika ya, maka bilangan bukan prima dan mengubah status menjadi False
            status = False
            break
        # Jika tidak, maka lanjutkan ke pembagi berikutnya
        pembagi += 1

    # Jika status masih True, maka bilangan adalah prima dan ditambahkan ke list prima
    if status:
        prima.append(bilangan)

    # Lanjutkan ke bilangan berikutnya
    bilangan += 1

print("Deret bilangan prima dari 1 sampai ", N, " adalah: ")
print(prima)