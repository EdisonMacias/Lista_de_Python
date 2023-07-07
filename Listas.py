class Metodos():
    def ingreso(self,lis,tam):
        i=0
        while(i<tam):
            print("Ingrese el [",i,"] valor de la lista")
            num=int(input("numero "))
            lis.append(num)
            i=i+1
            
    def ingreso_posicion(self, lis):
        p = int(input("Ingrese la posicion en donde desea insertar: "))
        d = int(input("Ingrese el dato a ingresar: "))
        lis.insert(p, d)
            
    def impresion(self,lis):
        if len(lis) != 0:
            for i in range(len(lis)):
                print(lis[i])
        else:
            print("Lista vacia")
            
    def borrar_todo(self,lis):
        lis.clear()
        
    def borrar_posicion(self, lis):
        p = int(input("Ingrese la posicion en donde desea borrar: "))
        lis.pop(p)  
        
    def contar_Repetidos(self,lis):
        num = int(input("Ingrese el numero: "))
        print(lis.count(num))
        
    def revertir_lista(self,lis):
        lis.reverse()
        
    def ascendente(self,lis):
        lis.sort()
        
    def descendente(self,lis):
        lis.sort(reverse=True)
