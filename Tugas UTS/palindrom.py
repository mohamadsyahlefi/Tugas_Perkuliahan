print('\n------MENYATAKAN KALIMAT PALINDROM ATAU BUKAN------\n')

kalimat = input("Masukkan kalimat: ")

kalimat = kalimat.lower()

kalimat = kalimat.replace(" ", "")
kalimat = kalimat.replace(",", "")
kalimat = kalimat.replace(".", "")
kalimat = kalimat.replace("!", "")
kalimat = kalimat.replace("?", "")
kalimat = kalimat.replace("'", "")

balik = kalimat[::-1]

if kalimat == balik:
    print("Kalimat tersebut adalah palindrom")
else:
    print("Kalimat tersebut bukan palindrom")
