#definimos una lista vacia
lista=[]
#disponemos un ciclo de 5 vueltas
valor = ""
while valor != "*":
    valor=input("Ingrese un valor entero o ingrese * para terminar: ")
    if valor == "*":
        break
    lista.append(int(valor))

maximoValor = max(lista)

#for n in range (2, max(lista)):


#imprimimos la lista    
print(lista)


"""
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo,", n, "es divisor")
            return
    print("Es primo")
    return
es_primo(64)
"""
