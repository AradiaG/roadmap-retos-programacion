"""
Operadores
"""
#Operadores aritméticos
print (f"Suma: 10 + 3 = {10 + 3}")
print (f"Resta: 10 - 3 = {10 - 3}")
print (f"Multiplicación: 10 * 3 = {10 * 3}")
print (f"División: 10 / 3 = {10 / 3}")
print (f"Módulo: 10 % 3 = {10 % 3}")
print (f"Exponente: 10 ** 3 = {10 ** 3}")
print (f"División entera: 10 // 3 = {10 // 3}")

#Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que que: 10 <= 3 es {10 <= 3}")

#Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 and 5 - 1 ==4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 or 5 - 1 ==4}")
print(f"NOT !: 10 + 3 == 13 not 5 - 1 == 4 es {not 5 - 2 ==4}")

#Operadores de asignación
my_number = 11    #Asignar valor 11 a la var
print(my_number)  
my_number += 1    #Esto es suma y asignación
print(my_number)
my_number *= 2    #Multiplicación y asignación
print(my_number)
my_number /= 2    #División y asignación
print(my_number)
my_number -= 1    #Resta y asignación
print(my_number)
my_number %= 3    #Módulo y asignación
print(my_number)
my_number **= 5    #Exponente y asignación
print(my_number)
my_number //= 3    #División entera y asignación
print(my_number)

#Operadores de identidad (Comparar valores de posición de memoria)
my_new_number = my_number
print(f"My_number is my_new_number es {my_number is my_new_number}")
print(f"My_number is not my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia (Algo pertenece a algo)
print(f"O in Rosy = {'o' in 'Rosy'}")
print(f"O not in Rosy = {'o' not in 'Rosy'}")

#Operadores de bit (Para trabajar sobre números enteros)
a = 10 # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}") #0010

"""
Estructuras de control
"""
#Condicionantes

my_string = "García"

if my_string == "AradíaH":
    print("My_string es 'AradíaG'")
elif my_string == "García":
    print("my_string es 'García'")
else:
    print("my_string no es 'AradíaG'")

#Iterativas

for i in range(1):
    print(i)
    
i = 0

while i <= 9:
    print(i)
    i +=1

#Manejo de excepciones
try: 
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
EXTRA
"""
for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)