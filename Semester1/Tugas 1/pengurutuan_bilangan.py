angkainput = []
x = int(input('Berapa banyak angka yang ingin di masukkan : '))
for i in range(x):
    angka = int(input('Masukkan angka : '))
    angkainput.append(angka)
print('Angka sebelum diurutkan : ', angkainput)
angkainput.sort()
print('Angka sesudah diurutkan', angkainput)