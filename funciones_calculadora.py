from os import system
def factorizar (n: int) -> int:
    """Factoreo de un numero

    Args:
        n (int): numero a factorizar

    Returns:
        int: numero factorizado
    """
    fact = 1
    for i in range (2 , n + 1):
        fact *= i
    return fact



def sumar(a:int,b:int) -> int:
    """suma 2 elementos

    Args:
        a (int): primer elemento
        b (int): segundo elemento

    Returns:
        int: la suma de los dos elementos
    """
    return a+b


def restar (a : int,b:int)->int:
    """resta dos numeros

    Args:
        a (int): primer elemento
        b (int): segundo elemento

    Returns:
        int: la resta de a y b
    """
    return a-b

def dividir (a:int,b:int)->float:
    """dividir 2 numeros

    Args:
        a (int): dividendo
        b (int): divisor

    Returns:
        float: resultado de la division
    """
    try:
        a/b
    except ZeroDivisionError:
        print("No es posible dividir por 0")
    else :
        return a/b
    

def multiplicar (a:int,b:int) ->int:
    """multiplicacion de dos numeros

    Args:
        a (int): primer elemento
        b (int): segundo elemento

    Returns:
        int: la multiplicacion de a y b
    """
    return a * b

def pausar ():
    return system("pause")


def limpiar_pantalla ():
    return system ("cls")

def preguntar(mensaje) -> bool:
    rta = input (mensaje) .lower()
    return rta == "si"



def calculadora_menu ():
    limpiar_pantalla()
    print("   MENU DE OPCIONES : ")
    print("1- Ingresar el primer valor ")
    print("2- Ingresar el segundo valor ")
    print("3- Calcular operaciones ")
    print("4- Salir ")
    
    return input (" ingrese el nro de operacion que desea : ")
   
    
        
        

