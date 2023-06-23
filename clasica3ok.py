
###Funcion Verificacion Numeros Ingresados###
def verificar(valor):
    """Esta funcion permite realizar la 
    verificacion del ingreso de un numero, 
    pudiendo este ser decimal"""
    salida_verificar = True
    try:
        float(valor)
    except ValueError:
        print ("\nINCORRECTO > INGRESE UN NUMERO")
        salida_verificar = False
    return salida_verificar

###Funcion Verificacion Operando###
def verificar_op(valorop):
    """Esta funcion permite la verificacion del 
    ingreso correcto de los operando + - x / 
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
    elif valorop == "/":
        salida_verificar = True
    else: 
        print("\n> OPERADOR INCORRECTO")
        salida_verificar = False
    return salida_verificar
 
resultado= 0

###BIENVENIDA CALC CLASICA###
print ("\nCALCULADORA CLASICA") 
print ("---------------------")

###Verificacion num1 que sea digitos###
numero_ok = False
while numero_ok == False:
    num1 = input("\n> Ingrese un numero: ") ###SE PIDE PRIMER VALOR###
    numero_ok = verificar (num1)
num1=float(num1)

###Menu Operando Calculadora Clasica###

###Fn de verificacion op###
operacion_ok = False
while operacion_ok == False:
    operacion = input("\n+  Suma\n-  Resta\nx  Multiplicacion\n/  Division\n=  Salir\n\nSeleccione Opcion: ")
    operacion_ok = verificar_op (operacion)
operacion = operacion

###Operaciones###
while operacion == "+" or operacion == "-" or operacion == "x" or operacion == "/":
    
    numero_ok = False
    while numero_ok == False:
        num2 = input("\n> Ingrese un numero: ")###SE PIDE SEGUNDO VALOR###
        numero_ok = verificar (num2)
    num2=float(num2)

    if(operacion == "+"):
        resultado=num1+num2
        print((f"{num1} + {num2} ="), resultado)
        
    elif(operacion == "-"):
        resultado=num1-num2
        print((f"{num1} - {num2} ="), resultado)

    elif(operacion == "x"):
        resultado=num1*num2
        print((f"{num1} x {num2} ="), resultado)

    elif(operacion == "/"):
        resultado=num1/num2
        print((f"{num1} / {num2} ="), resultado)

    elif(operacion == "="):
        fin = True    
    operacion=input("\n+  Suma\n-  Resta\nx  Multiplicacion\n/  Division\n=  Salir\n\nSeleccione Opcion: ")
    
    num1=resultado    

print(f"{resultado}")