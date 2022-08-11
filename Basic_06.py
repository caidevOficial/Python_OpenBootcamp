
weight = float(input('Ingresa tu peso en kg: '))
heigth = float(input('Ingresa tu altura en metros: ').replace(',', '.'))

IMC = round(weight / (heigth**2), 2)
print(f'Tu IMC es: {IMC}')