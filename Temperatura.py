import os
import sys

print ("--------------------------------------------------------")
print ("-------------Bienvenido a la Temperatura----------------")
print ("--------------------------------------------------------\n")

x = True
y = True

def error ():
    print ("Esta opcion no existe, ingrese una opcion valida...")
    raiz() 

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

#------------------------------------------------------------------------------------------------------------------------

def eleccion ():
    print ("Elige tus opciones:")
    print ("(1) Convertir de °C a °F")
    print ("(2) Convertir de °C a °K")
    print ("(3) Convertir de °F a °C")
    print ("(4) Convertir de °F a °K")
    print ("(5) Convertir de °K a °C")
    print ("(6) Convertir de °K a °F\n")

def cuestion ():
    print ("(1) si")
    print ("(2) no\n")
    terminar = int(input ("¿Desea terminar?: "))
    if terminar == 1:
        clear_screen()
        y = False
    elif terminar == 2:
        clear_screen()
        raiz ()

def first ():
    r11 = int(input("Escriba el numero que quiere convertir: "))
    var11 = r11
    var12 = var11 * 1.8
    var13 = var12 + 32
    print ("°F =", var11, "x 1.8 + 32\n°F =", var12,"+ 32\n°F =", var13,"\n")
    
    cuestion()


def second ():
    r12 = int(input("Escriba el numero que quiere convertir: "))
    var21 = r12
    var22 = var21 + 273
    print ("°K =", var21, "-273\n°K =", var22,"\n")

    cuestion()

def threeth():
    r13 = int(input("Escriba el numero que quiere convertir: "))
    var31 = r13
    var32 = var31 - 32
    var33 = var32 / 1.8
    print ("°C = (", var31,"- 32 ) / 1.8\n°C =", var32, "/ 1.8\n°C =", var33, "\n")

    cuestion()

def fourth ():
    r14 = int(input("Escriba el numero que quiere convertir: "))
    var41 = r14
    var42 = var41 - 32
    bla = 0.5 * var42
    var43 = bla + 273
    print ("°K = 5/9 (", var41,"- 32 ) + 273\n°K = 5/9", var42, "+ 273\n°K = 0.5 x", var42,"+ 273\n°K =",var43, "\n")

    cuestion()

def fiveth ():
    r15 = int(input("Escriba el numero que quiere convertir: "))
    var51 = r15
    var52 = var51 - 273
    print ("El resultado es: ", var52)
    
    cuestion()

def sixth ():
    r16 = int(input("Escriba el numero que quiere convertir: "))
    var61 = r16
    var62 = var61 - 273
    num = 1.8 * var62
    var63 = num + 32
    print ("El resultado es: ", var63)
    
    cuestion()

def raiz ():
    if x == True:
        y = True
        eleccion()
        op = int(input("Elige una opcion de acuerdo a su numero: "))
        
        clear_screen()
        
        if op ==1:
            first()
    
        elif op ==2:
            second()

        elif op ==3:
            threeth()

        elif op ==4:
            fourth()

        elif op ==5:
            fiveth()

        elif op ==6:
            sixth()

        else:
            error()
            
raiz()