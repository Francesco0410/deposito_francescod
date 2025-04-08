lista = []
x = True
while x:
    numero = int(input("inserisci un numero da aggiungere:"))
    lista.append(numero)
    if len(lista) < 4:
        for i in lista:
            print(i ** 2)
    else:
        x = False
print("la lista è:", lista)
