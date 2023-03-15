#definimos una lista vacia
lista=[]
#disponemos un ciclo de 5 vueltas
valor = ""
while valor != "*":
    valor=input("Ingrese un valor entero o ingrese * para terminar: ")
    if valor == "*":
        break
    lista.append(int(valor))

#imprimimos la lista    
print(lista)

