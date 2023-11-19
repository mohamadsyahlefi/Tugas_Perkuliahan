print('\nPROGRAM MENGHITUNG SUHU\n')

celcius = float(input('Masukan suhu dalam celcius : '))
print('Suhu adalah :', celcius, 'Celcius')

# Reamur
reamur = (4/5)*celcius
print('Suhu adalah :', reamur, 'Reamur')

# Fahrenheit
fahrenheit = (9/5)*celcius + 32
print('Suhu adalah :', fahrenheit, 'Fahrenheit')

# Kelvin
kelvin = celcius + 273
print('Suhu adalah :', kelvin, 'Kelvin')
