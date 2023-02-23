#--------------Ejercicio While--------------

global numeroP
global numeroS


operaciones = """¿Qué operación desea hacer?

Ingresa 1 para sumar
Ingresa 2 para Dividir
Ingresa 3 para Potenciación
Ingresa 4 para Multiplicar
Ingresa 5 para sacar la Raíz cuadrada
Ingresa 6 para cambiar los números que ingresaste
Ingresa 7 para Salir """


numeroP = int(input("Ingresa el primer número: "))
numeroS = int(input("Ingresa el segundo número: "))

opciones = 0

while opciones != 7 :

    opciones = int(input(operaciones))

    if opciones == 1 :

        suma = numeroP + numeroS
        print(numeroP, "+", numeroS, "=" , suma)

    elif opciones == 2 :

        dividir = numeroP / numeroS

        if numeroP == 0 or numeroS == 0 :
        
            print("Para dividir debes ingresar un número diferente a 0")

        else :

            print(numeroP, "/", numeroS, "=", dividir)

    elif opciones == 3 :

        potencia = numeroP ** numeroS
        print(numeroP, "potenciado", numeroS, "=", potencia)

    elif opciones == 4 :

        multiplicacion = numeroP * numeroS
        print(numeroP, "*", numeroS, "=", multiplicacion )

    elif opciones == 5 :

        raizCuadP = numeroP ** (1/2)
        print( "√" , numeroP, "=", raizCuadP)

        raizCuadS = numeroS ** (1/2)
        print( "√" , numeroS, "=", raizCuadS)


    elif opciones == 6 :

        cambiarP = int(input("Ingresa el nuevo primer número"))
        cambiarS = int(input("Ingresa el nuevo segundo número"))

        numeroP = cambiarP
        numeroS = cambiarS

        print("Los nuevos números son:", numeroP, "y", numeroS)

    elif opciones == 7 :

        print("Has seleccionado salir, ¡Hasta pronto!")
        break

    else :

        print("Opción inválida, intenta de nuevo")

    



    
