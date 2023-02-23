#--------------Ejercicio 4--------------

notaDesarrollo = float(input("Ingrese su nota de Desarrollo de Software"))
notaMate = float(input("Ingrese su nota de Matemáticas"))
notaLogica = float(input("Ingrese su nota de Lógica de programación"))

resultado = notaDesarrollo + notaMate + notaLogica / 3

if resultado >= 3.0 :

    print("Usted aprobó")

else :

    print("Usted ha reprobado")


