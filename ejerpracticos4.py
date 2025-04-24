# Solicitar dos números e indicar cuál es mayor o si son iguales
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 > num2:
    print("El primer número es mayor.")
elif num1 < num2:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")

# Solicitar la edad y determinar si la persona es menor de edad
edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

# Comparar dos cadenas de texto e indicar si son iguales o distintas
cadena1 = input("Introduce la primera cadena de texto: ")
cadena2 = input("Introduce la segunda cadena de texto: ")

if cadena1 == cadena2:
    print("Las cadenas son iguales.")
else:
    print("Las cadenas son distintas.")