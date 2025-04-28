#ejercicio2

nota=int(input("ingrese su calificacion "))
if nota>=60 and nota<=100:
    print("APROBO")
elif nota<60 and nota>=0:
    print("REPROBO")
else:
    print("NOTA INVALIDA")