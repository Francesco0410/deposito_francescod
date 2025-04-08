lista = []
x = True
while x:
    if len(lista) < 4:
    numero = int(input("inserisci un numero da aggiungere:"))
    lista.append(numero)
        for i in lista:
            print(i ** 2)
    else:
        x = False
print("la lista è:", lista)
