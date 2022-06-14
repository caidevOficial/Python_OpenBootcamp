
initial_number = int(input("Numero inicial para mostrar pares: "))
final_number = int(input("Numero final para mostrar pares: "))

print('Numeros pares:')
for i in range(initial_number, final_number + 1):
    if i % 2 == 0:
        print(i, end=' | ')