print('\n------PROGRAM MENGHITUNG KEUNTUNGAN DEPOSITO BANK TOET------\n')

print('Produk Deposito :\n','1. Pasti cuan(bunga 10% per-tahun)\n\n')
jumlah_uang_deposito = int(input('Masukkan nominal uang deposito anda dalam rupiah (tanpa titik koma) : '))
print('\nUang anda sebesar : Rp', jumlah_uang_deposito, '\n')

tahun = int(input('Berapa tahun anda ingin menyimpannya : '))
print('\nAnda akan menyimpan deposito selama ', tahun, 'tahun\n\n')

bunga = (10/100)* jumlah_uang_deposito
total_bunga = bunga * tahun
total_keuntungan = jumlah_uang_deposito + total_bunga

print('Total uang anda adalah Rp',int(total_keuntungan), 'dengan deposito selama ', tahun,'tahun\n')