print('\n------MENHITUNG BILANGAN FAKTORIAL------\n')
n = int(input("Masukkan nilai n: "))

if n == 0 or n == 1:
    print(1)

else:
    hasil = 1
    for i in range(n, 0, -1):
        hasil = hasil * i
    
    print(hasil)
