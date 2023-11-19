print('\n------PROGRAM MENGHITUNG PENGELUARAN GAJI------\n')

gaji_perJam = float(input('Masukkan gaji per jam yang anda inginkan : '))
jam_kerja_perMinggu = float(input('Masukkan jumlah jam kerja per Minggu : '))

pajak = 0.14

#Pendapatan sebelum pajak
gaji_sebelum_pajak = gaji_perJam * jam_kerja_perMinggu * 5

#Pendapatan setelah pajak
gaji_setelah_pajak = 0.14 * gaji_sebelum_pajak

#Pengeluaran untuk membeli pakaian & aksesoris (10% dari pendapatan bersih)
pengeluaran_pakaian_aksesoris = 10/100 * gaji_setelah_pajak

#Pengeluaran untuk membeli alat tulis (1% dari pendapatan bersih)
pengeluaran_alatTulis = 1/100 * gaji_setelah_pajak

#Jumlah uang yang di sedekahkan (25% dari sisa pendapatan setelah pengeluaran)
sedekah = 25/100 * (gaji_setelah_pajak - pengeluaran_pakaian_aksesoris - pengeluaran_alatTulis)

#Jumlah uang untuk anak yatim (30% dari uang yang di sedekahkan)
anak_yatim = 30/100 * sedekah

#Jumlah uang untuk kaum dhuafa (70% dari uang yang di sedekahkan)
dhuafa = 70/100 * sedekah

#Output semuanya
print('\n\nPendapatan sebelum pajak adalah Rp', gaji_sebelum_pajak)
print('Pendapatan setelah pajak adalah Rp', gaji_setelah_pajak)
print('Jumlah uang membeli pakaian dan aksesoris adalah Rp',pengeluaran_pakaian_aksesoris)
print('Jumlah uang membeli alat tulis adalah Rp',pengeluaran_alatTulis)
print('Jumlah uang untuk di sedekahkan adalah Rp',sedekah)
print('Jumlah uang yang diterima anak yatim adalah Rp', anak_yatim)
print('Jumlah uang yang diterima kaum dhuafa adalah Rp', dhuafa)