#definimos una lista vacia
lista=[]
#disponemos un ciclo de 5 vueltas

valor=input("Ingrese un valor entero, ingrese * para terminar: ")

while valor != "*":
    lista.append(int(valor))

#imprimimos la lista    
print(lista)

