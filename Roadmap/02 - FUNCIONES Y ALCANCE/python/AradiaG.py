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

#Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "python"

greet, name = multiple_return_greet()
print(greet)
print(name)

#Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"¡Hola, {name}!")

variable_arg_greet("Python", "Brais", "Rosy", "Comunidad")

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"¡{value} ({key})!")

variable_key_arg_greet(
language="Python",
name= "Brais",
alias="Rosy",
edad= 32
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python")
    inner_function()

outer_function()

"""
Funciones de lenguaje (built-in)
"""

print(len("Rosy"))
print(type(36))

print("Rosy".upper())

"""
Variables locales y globales
"""

global_var = "Pythones"

print(global_var)

def hello_python():
    print(f"Hola {global_var}!")

"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text_1}{text_2}")
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2) 
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Rosy","Tita"))




