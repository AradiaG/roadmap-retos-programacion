#Listas
my_list = ["Rosy", "María", "Isa", "Martha"]
print(my_list)
my_list.append("Castor") #Inserción
print(my_list)
my_list.remove("María") #Eliminación
print(my_list)
print(my_list[0]) #Acceso
print(my_list)
my_list.sort() #Ordenación

#Tuplas   (Podemos guardar más de un dato, inmutables)
my_tuple: tuple = ("Rosy", "González", "Arizona", "32")

my_tuple = tuple (sorted(my_tuple)) #Nos regresa una lista, ya no es inmutable
print(my_tuple)
print(type(my_tuple))
