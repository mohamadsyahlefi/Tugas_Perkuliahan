print('\n------PROGRAM MENGHITUNG KEUNTUNGAN DEPOSITO------\n')

print('Bunga sebesar 10% per-tahun\n\n')

jumlah_uang = int(input('Masukkan nominal uang anda dalam rupiah (tanpa titik koma) : '))
print('\nUang anda sebesar : Rp', jumlah_uang, '\n')

jumlUang_berbunga = int(input('Masukkan nominal uang yang ingin anda capai (tanpa titik koma) : '))
print('\nNominal uang yang ingin di capai sebesar : Rp', jumlUang_berbunga,'\n')


bunga_berbunga = jumlUang_berbunga - jumlah_uang
bunga = (10/100)* jumlah_uang
total_bunga = bunga_berbunga / bunga

print('Waktu yang dibutuhkan untuk mencapai Rp',jumlUang_berbunga, 'adalah ', int(total_bunga),'tahun\n')
