num1 = 0
den1 = 0
num2 = 0
den2 = 0
res = 0
num3 = 0
den3 = 0
rta= 0

###Fn Operaciones Num Den###
def suma (num1,den1,num2,den2):
    """Esta funcion es el procedimiento 
    de resolución para la suma de fracciones"""
    den3 = den1*den2
    num_aux1 = num1*den2
    num_aux2 = num2*den1
    num3 = num_aux1+num_aux2
    res= num3, den3
    print(f"{res}")
    return res

def resta (num1,den1,num2,den2):
    """Esta funcion es el procedimiento de 
    resolución para la resta de fracciones"""
    den3 = den1*den2
    num_aux1 = num1*den2
    num_aux2 = num2*den1
    num3 = num_aux1-num_aux2
    res= num3, den3
    print(f"{res}")
    return res

def multi (num1,den1,num2,den2):
    """Esta funcion es el procedimiento de 
    resolución para la multiplicacion de fracciones"""
    num3 = num1*num2
    den3 = den1*den2
    res= num3, den3
    print(f"{res}")
    return res

def div (num1,den1,num2,den2):
        """Esta funcion es el procedimiento de 
        resolución para la division de fracciones"""
        num3 = num1*den2
        den3 = den1*num2
        res= num3, den3
        print(f"{res}")
        return res

###Funcion Verificacion Numeros Ingresados###
def verificar(valor):
    """Esta funcion permite realizar la 
    verificacion del ingreso de un numero, 
    exclusivamente entero"""
    salida_verificar = True
    try:
        int(valor)
    except ValueError:
        print ("\nINCORRECTO > INGRESE UN NUMERO ENTERO")
        salida_verificar = False
    return salida_verificar

###Funcion Verificacion Operando###
def verificar_op(valorop):
    """Esta funcion permite la verificacion del 
    ingreso correcto de los operando + - x : 
    ejecutando un aviso de "Operando Incorrecto" 
    si se ingresa otra cosa"""
    if valorop == "=":
        salida_verificar = True
    elif valorop == "+":
        salida_verificar = True
    elif valorop == "-":
        salida_verificar = True 
    elif valorop == "x":
        salida_verificar = True
    elif valorop == ":":
        salida_verificar = True
    else: 
        print("\n> OPERADOR INCORRECTO")
        salida_verificar = False
    return salida_verificar

def calculadora_fra():
    sal = False

    ###BIENVENIDA CALC FRACCIONARIA###
    print ("\nCALCULADORA FRACCIONARIA") 
    print ("-------------------------")

    ###Pedido de primer numerador y denominador###


    cerrar = ""
    salir = False
    while salir == False:

    ###Verificacion Numerador###
        numero_ok = False
        while numero_ok == False:
            num1 = input("\n> Ingrese el numerador: ") ###SE PIDE NUMERADOR num1###
            numero_ok = verificar (num1)
        num1=int(num1)

    ###Verificacion Denominador###
        numero_ok = False
        while numero_ok == False:
            den1 = input("\n> Ingrese el denominador: ") ###SE PIDE DENOMINADOR den1###
            numero_ok = verificar (den1)
        den1=int(den1)

        while sal == False:
            ###Pedido de Operando###
            #op = input("\n+  Suma\n-  Resta\nx  Multiplicacion\n:  Division\n\n>Ingrese un operador: ")
            
            ###Verificacion Operando###
            operacion_ok = False
            while operacion_ok == False:
                operacion = input("\n+  Suma\n-  Resta\nx  Multiplicacion\n:  Division\n=  Resultado\n\n>Ingrese un operador: ")
                operacion_ok = verificar_op (operacion)
            operacion = operacion
            #check()

        ###Pedido 2do Numerador y Verificacion###
            numero_ok = False
            while numero_ok == False:
                num2 = input("\n> Ingrese el numerador: ") ###SE PIDE NUMERADOR num2###
                numero_ok = verificar (num2)
            num2=int(num2)
                #num2 = int(input("\n> Ingrese el numerador: "))

            ###Pedido de 2do Denominador y Verificacion###
            numero_ok = False
            while numero_ok == False:
                den2 = input("\n> Ingrese el denominador: ") ###SE PIDE DENOMINADOR den2###
                numero_ok = verificar (den2)
            den2=int(den2)
                #den2 = int(input("\n> Ingrese el denominador: "))

            if operacion == "+":
                    den3 = den1*den2
                    num3 = num1*den2 + num2*den1  
                    print(f"{num1} / {den1} + {num2} / {den2} = {num3} / {den3}")

            elif operacion  == "-":
                    den3 = den1*den2
                    num3= num1*den2 - num2*den1  
                    print(f"{num1} / {den1} - {num2} / {den2} = {num3} / {den3}")

            elif operacion  == "x":
                    den3 = den1*den2
                    num3= num1*num2
                    print(f"{num1} / {den1} x {num2} / {den2} = {num3} / {den3}")

            elif operacion  == ":":
                    den3 = den1*num2
                    num3= num1*den2  
                    print(f"{num1} / {den1} : {num2} / {den2} = {num3} / {den3}")

            elif operacion == "=":
                rta=res
                sal = True
                print(f"{rta}")
            cerrar = input("\nIngrese la letra s para salir o ENTER para continuar: ")
            if cerrar == "s":
                salir = True
                sal = True
                print ("FIN FRACCIONARIA\n")
                print("Gracias por usar Skynet\n")

        num1=num3
        den1=den3

        #print(rta)

calculadora_fra()