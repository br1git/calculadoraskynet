###CONVERSORA###
###Verifica y convierte a numero hexadecimal###
def verificar_hexa(cociente) : 
    salida = ""
    if cociente < 10 :
        salida = str(cociente)
    elif str(cociente) == "10":
        salida = "A"
    elif str(cociente) == "11":
        salida = "B"
    elif str(cociente) == "12":
        salida = "C"
    elif str(cociente) == "13":
        salida = "D"
    elif str(cociente) == "14":
        salida = "E"
    elif str(cociente) == "15":
        salida = "F" 
    return salida

###Funcion Verificacion Numeros Ingresados###
def verificar(valor):
    #Funcion que Verifica que numeros ingresdos sean enteros, de no ser asi, avisa y lo pide nuevamente.
    salida_verificar = True
    try:
        int(valor)
    except ValueError:
        print ("INCORRECTO > INGRESE UN NUMERO")
        salida_verificar = False
    return salida_verificar
   
def dec_hexa() :
    #Funcion que realiza las operaciones de modulo y divicion para realizar la convercion, guardar e imprimir el resultado.
    cociente = 0
    resto = 0
    resultado = ""
    base = 16
    salir = False
    while salir == False :
        cociente_ok = False
        while cociente_ok == False :
            cociente = input("Ingrese un numero entero:  ")
            cociente_ok = verificar(cociente)
        cociente = int(cociente)
        num = cociente

        if cociente < base :
            res = verificar_hexa(cociente)
            print(f"{cociente} = {res}" )
            cerrar = input("Si desea salir ingrese la letra s o presione enter para Continuar: ")
            if cerrar == "s":
                salir = True#revisar salida

        while cociente >= base :
            resto = cociente % 16
            resultado =  verificar_hexa(resto) + str(resultado)
            cociente = cociente // 16
            if cociente < 16 :
                res_final = str(cociente) + str(resultado)    
                print(f"{num} = {res_final}")
                resultado = "" 
                cerrar = input("Si desea salir ingrese la letra s o presione enter para Continuar: ")
                if cerrar == "s":
                    #print("FIN")
                    salir = True





def dec_octal():
    """Recive un numero de base decimal por teclado y lo convierte a base octal"""
    resultado = ""
    cociente = int(input("ingrese un num entero: "))
    while cociente >= 8:
        resto = cociente % 8
        resultado = str(resto) + resultado
        cociente = cociente // 8
    resultado = str(cociente) + str(resultado)
    print(resultado)   
    return resultado
#print(dec_octal())

def dec_bin():
    """Recive un numero de base decimal por teclado y lo convierte a base binaria"""
    resultado = ""
    cociente = int(input("Ingrese un num entero: "))
    while cociente >= 2 :
        resto = cociente % 2
        resultado = str(resto) + (resultado)
        cociente = cociente // 2
    resultado = str(cociente) + str(resultado)
    #print(resultado)
    return resultado
#print(dec_bin())

        ###MENU DE CALCULADORA###
def verificar_menu(opcion):
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

print("\n###BIENVENIDO A LA CONVERSORA###\n\n >")
salir = False
while salir == False :
    opcion_ok = False
    while opcion_ok == False:
        opcion = input("\n1 > Conversora Decimal a Hexa\n2 > Conversora Decimal a Octal\n3 > Conversora Decimal a Binario\n4 > Salir (off)\n\n> Seleccione Opcion: ")
        opcion_ok = verificar_menu (opcion)
    opcion = opcion

    if opcion == "1":
        dec_hexa()
        print(dec_hexa())
    elif opcion == "2":
        dec_octal()
        print(dec_octal())
    elif opcion == "3":
        res = dec_bin()
        print(f"\nResultado = {res}")
    elif opcion == "4" :
        salir = True
print("FIN")