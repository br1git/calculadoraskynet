###Encendido de la calculadora###
encendido = (input("\nIngrese ON para encender la calculadora: ")) 
ON = "ON"
while encendido != ON:    
    encendido = (input("Ingrese ON con Mayus para encender la calculadora: "))

###BIENVENIDA CALCULADORA###
print("\n###BIENVENIDO A CALCULADORA SKYNET###")
print("--------------------------------------\n")

###Fn Verificacion Menu General###
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

menu_global = False
while menu_global == False:
    ###MENU CALCULADORA GENERAL###
    opcion_ok = False
    while opcion_ok == False:
        opcion = input("1 > Calculadora Clasica\n2 > Calculadora de Fracciones\n3 > Calculadora de Conversiones\n4 > Salir (Off)\n\nSeleccione Opcion: ")
        opcion_ok = verificar_menu (opcion)
    opcion = opcion

    #opcion = False
    #while opcion != "4":

    if opcion == "1":
        import clasica3ok

    elif opcion == "2":
        import fraccionariatesteo

    elif opcion == "3":
        import conversora2ok

    elif opcion == "4":
        print("\n> Gracias por usar Skynet")
        menu_global = True
