#edad y licencia para determinar si puede manejar

edad=int(input("ingresa tu edad "))
lic=str(input("tienes licencia de conduccion? (si/no)")).lower()

if edad >=18 and lic =='si':
    print("puedes conducir")
else:
    print("no puedes conducir")

#Solicita si una persona tiene experiencia laboral y título universitario

exp=input("tienes experiencia laboral? (si/no) ").lower()
titulo=input("tienes titulo universitario? (si/no) ").lower()

if exp=='si' and titulo=='si':
    print("aplicas para nuestra oferta laboral")
else:
    print("no aplicas para nuestra oferta")


#Dado un número, determina si está en el rango de 10 a 50 

