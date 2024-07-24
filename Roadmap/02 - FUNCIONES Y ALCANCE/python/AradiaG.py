"""
Funciones definidas por el usuario
"""

# Simple

def greet():
    print("Hola, Aradia")
greet()

#Con retorno

def return_greet():
    return "Hola, AradíaG"
print(return_greet())

#Con un argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Aradia")

#Con argumentos

def args_greet(greet, name):
    print(f"Hola, {greet},{name}!")

args_greet("Aradia","G")

#Con argumento predeterminado

def default_arg_greet(name="Py"):
    print(f"Hola, {name}!")


default_arg_greet()
default_arg_greet("Sí tiene")

#Con argumentos y retorno

def return_args_greet(greet, name):
    return f"Hola, {greet},{name}!"
print(return_args_greet("Hi", "Brais"))