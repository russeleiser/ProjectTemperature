print ("--------------------------------------------------------")
print ("-------------Bienvenido a la Temperatura----------------")
print ("--------------------------------------------------------\n")

x = 0
while x < 10000:

    print ("Elige tus opciones:")

    print ("(1) Convertir de °C a °F")
    print ("(2) Convertir de °C a °K")
    print ("(3) Convertir de °F a °C")
    print ("(4) Convertir de °F a °K")
    print ("(5) Convertir de °K a °C")
    print ("(6) Convertir de °K a °F\n")

    op = int(input("Elige una opcion de acuerdo a su numero: "))

    if op ==1:
        r11 = int(input("Escriba el numero que quiere convertir: "))
        var11 = r11
        var12 = var11 * 1.8
        var13 = var12 + 32
        print ("°F =", var11, "x 1.8 + 32\n°F =", var12,"+ 32\n°F =", var13,"\n")
    
    elif op ==2:
        r12 = int(input("Escriba el numero que quiere convertir: "))
        var21 = r12
        var22 = var21 + 273
        print ("°K =", var21, "-273\n°K =", var22,"\n")

    elif op ==3:
        r13 = int(input("Escriba el numero que quiere convertir: "))
        var31 = r13
        var32 = var31 - 32
        var33 = var32 / 1.8
        print ("°C = (", var31,"- 32 ) / 1.8\n°C =", var32, "/ 1.8\n°C =", var33, "\n")

    elif op ==4:
        r14 = int(input("Escriba el numero que quiere convertir: "))
        var41 = r14
        var42 = var41 - 32
        bla = 0.5 * var42
        var43 = bla + 273
        print ("°K = 5/9 (", var41,"- 32 ) + 273\n°K = 5/9", var42, "+ 273\n°K = 0.5 x", var42,"+ 273\n°K =",var43, "\n")

    elif op ==5:
        r15 = int(input("Escriba el numero que quiere convertir: "))
        var51 = r15
        var52 = var51 - 273
        print ("El resultado es: ", var52)

    elif op ==6:
        r16 = int(input("Escriba el numero que quiere convertir: "))
        var61 = r16
        var62 = var61 - 273
        num = 1.8 * var62
        var63 = num + 32
        print ("El resultado es: ", var63)

    else:
        print ("Esta opcion no existe, ingrese una nueva opcion...")
    
    x = x + 1
