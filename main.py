print("Hola equide, este archivo está conectado con Git y GitHub")
print("Probaremos hacer una calculadora basica")


def Suma():
    v1 = int(input("Ingrese el primer valor: \t"))
    v2 = int(input("Ingrese el segundo valor \t"))
    suma = v1 + v2

    print(f"La suma de los números {v1} + {v2} es de: {suma}")

def Resta():
    v1 = int(input("Ingrese el primer valor: \t"))
    v2 = int(input("Ingrese el segundo valor \t"))
    resta = v1 - v2
    print(f"La suma de los números {v1} - {v2} es de: {resta}")



def Menu():
    print("\n Menu de calculadora \n")
    print("1. Suma")
    print("2. Resta")
    while True:
        try:
            op = int(input("Ingrese una de las opciones: \t"))
            if (op < 1 or op > 2):
                print("ERROR... Intente de nuevo")
            else:
                break
        except:
            print("Error de formato... Intente de nuevo")

    match op:
        case 1:
            Suma()
        case 2:
            Resta()
Menu()