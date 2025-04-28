import random

numero_secreto = random.randint(1, 10)
intentos = 0
max_intentos = 3

print("Adivina el número entre 1 y 10. ¡Tienes 3 intentos!")

while intentos < max_intentos:
    adivinanza = int(input(f"Intento {intentos + 1}: Ingresa tu número: "))
    intentos += 1

    if adivinanza == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif adivinanza < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if adivinanza != numero_secreto:
    print(f"Lo siento, no lograste adivinar. El número era {numero_secreto}.")