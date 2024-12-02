print('\n------PROGRAM MENGHITUNG KEUNTUNGAN(%)------\n')

print('Harga emasmu saat beli adalah Rp.650.000')
print('Harga emas sekarang adalah Rp.685.000')
print('Harga emas mendatang adalah Rp.715.000\n')

hargaEmas_awal_Per_Gram = 650000
jumlah_awal_emas = float(input('Masukkan jumlah emas yang kamu miliki dalam gram : '))
hargaEmas_sekarang_perGram = 685000

print('Total emasmu adalah', jumlah_awal_emas, 'Gram')

keuntungan_Rp = (hargaEmas_sekarang_perGram - hargaEmas_awal_Per_Gram) * jumlah_awal_emas
keuntungan_persen = (keuntungan_Rp / (hargaEmas_awal_Per_Gram * jumlah_awal_emas)) * 100

print('\n~~~Keuntunganmu Sekarang~~~\n')
print('Keuntungan sekarang adalah Rp', keuntungan_Rp)
print('Persentase keuntungan sekarang adalah ', keuntungan_persen, '%')

jumlahEmas_tambahan = int(input("\nMasukkan jumlah emas yang ingin dibeli dalam gram : "))
hargaEmas_PerGram_mendatang = 715000

print('Jumlah yang ingin dibeli dalam gram adalah', jumlahEmas_tambahan, 'Gram')
print('Jumlah emasmu yang akan datang adalah', jumlah_awal_emas + jumlahEmas_tambahan, 'Gram')

total_emas = jumlah_awal_emas + jumlahEmas_tambahan
total_biaya_beli = (hargaEmas_awal_Per_Gram * jumlah_awal_emas) + (hargaEmas_sekarang_perGram * jumlahEmas_tambahan)
keuntungan_Rp_mendatang = (total_emas * hargaEmas_PerGram_mendatang) - (jumlah_awal_emas * hargaEmas_awal_Per_Gram) - (jumlahEmas_tambahan * hargaEmas_sekarang_perGram)
keuntungan_persen_mendatang = (keuntungan_Rp_mendatang / total_biaya_beli) * 100

print('\n~~~Keuntungan Mendatang~~~\n')
print('Keuntungan mendatang adalah Rp', keuntungan_Rp_mendatang)
print('Persentase keuntungan mendatang adalah ', keuntungan_persen_mendatang, '%\n')
