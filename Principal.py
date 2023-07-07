from Listas import Metodos
Listas=[]
_tam=int(input("Ingrese el tamano de la Lista: "))
c=Metodos()
op = 0
while op != 10:
    print("*****Menu*****")
    print("1.- Ingresar datos")
    print("2.- Ingresar dato en una posicion especifica")
    print("3.- Imprimir datos")
    print("4.- Borrar todos los datos")
    print("5.- Borrar un dato especifico")
    print("6.- Contar las veces que se repite un dato")
    print("7.- Revertir lista")
    print("8.- Ordenar de manera ascendente")
    print("9.- Ordenar de manera descendente")
    print("10.- Salir")
    op = int(input())
    match op:
        case 1:
            print("****************************************")
            c.ingreso(Listas,_tam)
            print("****************************************")
        case 2:
            print("****************************************")
            c.ingreso_posicion(Listas)
            print("****************************************")
        case 3:
            print("****************************************")
            c.impresion(Listas)
            print("****************************************")
        case 4:
            print("****************************************")
            c.borrar_todo(Listas)
            print("****************************************")
        case 5:
            print("****************************************")
            c.borrar_posicion(Listas)
            print("****************************************")
        case 6:
            print("****************************************")
            c.contar_Repetidos(Listas)
            print("****************************************")
        case 7:
            print("****************************************")
            c.revertir_lista(Listas)
            print("****************************************")
        case 8:
            print("****************************************")
            c.ascendente(Listas)
            print("****************************************")
        case 9:
            print("****************************************")
            c.descendente(Listas)
            print("****************************************")
        case 10:
            print("****************************************")
            print("Adios!!!!!!!!!!!!")
            print("****************************************")
        case other:
            print("Opcion no valida!!!!!!!!!")