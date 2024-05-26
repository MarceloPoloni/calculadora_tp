from funciones_calculadora import *


 
def ingresar_primer_operando (): 
    a=None  
    while a is None:
            try :
                a = int(input (" ingrese el primer operando (A=X) : "))
                
            except ValueError:
                print( " ingrese un numero valido")
    return a
def ingresar_segundo_operando():
    b=None
    while b is None:
                try :
                    b = int(input (" ingrese el segundo numero (B=Y) : "))
                except ValueError:
                    print( " ingrese un numero valido")
    
    return b
          
def realizar_operaciones(a : int, b :int)-> int:
    print(f"Suma: {sumar(a, b)}")
    print(f"Resta: {restar(a, b)}")
    print(f"División: {dividir(a, b)}")
    print(f"Multiplicación: {multiplicar(a, b)}")
    print(f"el factorial de a es {factorizar(a)}")
    

def calculadora_opcion ():
        print(" Operaciones que se van a realizar :")
        print(" Suma ")
        print(" Resta ")
        print(" Multiplicación ")
        print(" División ")
        print(" Factorización de x")
        print(" ------------------")
        print(" --OPERACIONES--")
        print (realizar_operaciones(a,b))

    
    
a= None
b= None
bandera_primer_operando = False
bandera_segundo_operando= False
seguir = "si"
while seguir == "si":
    match calculadora_menu():
        case "1": 
            a = ingresar_primer_operando()
            bandera_primer_operando = True
            
            print (f"x = {a}")
        
        case "2" :
            if bandera_primer_operando:
                b = ingresar_segundo_operando()
                print(f"y = {b}")
                bandera_segundo_operando = True
            else :
                print("debe ingresar primer el primer operando")
        case "3":
            if bandera_primer_operando == True and bandera_segundo_operando == True:
                calculadora_opcion()
            else:
                print ("tiene que ingresar 2 operandos")
            
            
        case "4":
            bandera_primer_operando = False
            bandera_segundo_operando = False
            if preguntar("Usted quiere salir del programa? Si / NO :") :
                seguir = "no" 
            
    
    pausar()
  
            
   
    
    