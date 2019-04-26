##DETERMINE LA CLASIFICACION DEL TRIANGULO
L1 = int(input("INGRESE EL PRIMER LADO: "))
L2 = int(input("INGRESE EL SEGUNDO LADO: "))
L3 = int(input("INGRESE EL TERCER LADO: "))
if L1 == L2 == L3 :
     print("EL TRIANGULO ES EQUILATERO: ")
elif L1 == L2 and L1 != L3 and L2 != L3 :
     print("EL TRIANGULO ES ISOCELES: ")
elif L1 == L3 and L1 != L2 and L3 !=L2 :
     print("EL TRIANGULO ES ISOCELES: ")
elif L2 == L3 and L2 != L1 and L3 !=L1 :
     print("EL TRIANGULO ES ISOCELES: ")
else:
    print("ESTE TRIANGULO ES ESCALENO:")

