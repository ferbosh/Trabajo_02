# DETERMINAR EL COSTO DE LAS MANZANAS

kilo = float(input("CANTIDAD DE KILOS: "))
precio = 2
if 0 < kilo <= 2:
    print("EL PRECIO A PAGAR ES: ", (precio * kilo))
elif 2.01 < kilo <= 5:
    descuento = (0.1* precio)/100
    print("EL PRECIO A PAGAR ES: ", (precio - descuento))
elif 5.01 < kilo <= 10:
    descuento = (1.5 * precio)/100
    print("EL PRECIO A PAGAR ES: ",(precio - descuento))
elif 10.01 < kilo :
    descuento = (2.0 * precio)/100
    print("EL PRECIO A PAGAR :",(precio - descuento))
else :
    print("EL KILO INGRESADO NO ES VALIDO: ")
