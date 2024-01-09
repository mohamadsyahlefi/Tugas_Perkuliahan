print('\n------MENCARI DIGIT PALING KANAN SAMA------\n')

def cek_digit_belakang(a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10
    
    if digit_a == digit_b or digit_a == digit_c or digit_b == digit_c:
        return True
    else:
        return False

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

hasil = cek_digit_belakang(a, b, c)

print("Hasil:", hasil)
