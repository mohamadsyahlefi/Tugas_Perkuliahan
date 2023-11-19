print('\n------PROGRAM MENGHITUNG TAHUN KABISAT------\n')
# Tahun kabisat adalah tahun yang habis dibagi 4, kecuali jika juga habis dibagi 100 dan tidak habis dibagi 400

tahun = int(input("\nMasukkan tahun antara 1900-2020: "))

if tahun < 1900 or tahun > 2020:
    print("Tahun tidak valid")

else:
    if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
        print(tahun, " adalah tahun kabisat")
    else:
        print(tahun, " bukan tahun kabisat")