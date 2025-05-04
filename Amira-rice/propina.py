cuenta = int(input('Ingrese el total de su cuenta: '))
porcentaje  = int (input('Ingrese el valor de la propina: '))

propina = cuenta * ( porcentaje / 100)
total = cuenta + propina

print(f'El valor de la propina es: {propina}')
print(f'El total de la cuents es: {total}')

