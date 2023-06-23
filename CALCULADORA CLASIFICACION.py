def verificar_menu(opcion):
    """Esta funcion permite realizar 
    la verificacion del correcto ingreso 
    de opciones para el menu de las distintas 
    calculadoras y salida"""
    if opcion == "1":
        salida_verificar = True
    elif opcion == "2":
        salida_verificar = True
    elif opcion == "3":
        salida_verificar = True 
    elif opcion == "4":
        salida_verificar = True
    else: 
        print("\n> MENU INCORRECTO")
        salida_verificar = False
    return salida_verificar

opcion_ok = False
while opcion_ok == False:
    opcion = input("\n###BIENVENIDO A CALCULADORA SKYNET###\n\n1 > Calculadora Clasica\n2 > Calculadora de Fracciones\n3 > Calculadora de Conversiones\n4 > Salir (off)\n\nSeleccione Opcion: ")
    opcion_ok = verificar_menu (opcion)
opcion = opcion