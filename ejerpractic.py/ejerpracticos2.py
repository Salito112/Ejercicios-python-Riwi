# Declaración de variables de tipos básicos
entero = 11
flotante = 4.7
cadena = "salome, gonzalez, 18"
booleano = True

# Conversión de cadena numérica a entero y suma
cadena = "15"
numconvertido = int(cadena)
suma = numconvertido + 7
print("Resultado de la suma:", suma)

# Conversión de entrada de texto a número flotante y multiplicación por 2
decimal = input("Ingresa un número decimal: ")
numflotante = float(decimal)
resultado = numflotante * 2
print("El doble del número es:", resultado)

# Función para verificar si una cadena puede convertirse a número
texto=str(input("ingresa un texto para cambiar a numero"))
variable_condicion=False
try: 
    valor=int(texto)
    variable_condicion=True
except ValueError:
    variable_condicion=False

if variable_condicion==True:
    print("si se puede convertir a numero")

else:
    print("no se pudo convertir")
    

