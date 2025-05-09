name = input('Ingrese su nombre: \n')


print('Bienvenid@ ' + name)

age = int(input('Ingrese su edad: \n'))
dist = 100-age 

if age >= 0 and age <= 100:
    print('Le quedan ' + str(dist) + ' años para cumplir los 100')
elif age > 100:
    print('Usted ya cumplio 100 años \n')
else:
    print('Edad no valida\n')

with open('edad.txt','w') as archivo:
    archivo.write('Le faltan ' + str(dist) + ' años para cumplir los 100')
