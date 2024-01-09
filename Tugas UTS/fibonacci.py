print('\n------MENHITUNG FIBONACCI SECARA REKURSIF------\n')

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Masukkan nilai n: "))
hasil = fibonacci(n)

print("\nFibonacci dari", n, "adalah", hasil,'\n')
