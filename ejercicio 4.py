# CALCULAR EL PROMEDIO

p1 = int(input("Ingrese la primera nota: "))
p2 = int(input("Ingrese la segunda nota: "))
p3 = int(input("Ingrese la tercera nota: "))
promedio = (p1 + p2 + p3)/3

if p1 >= 7:
    print("Promocionado")
elif 7 < p2 <= 4:
    print("Regular")
elif p3 > 4:
    print("Desaprobado")
else:
    print("Fuera del rango")
