#Esercizio per capire se è numero primo o meno, vedendo se è pari.
lista_numeri = []
while len(lista_numeri) < 5: #mettiamo 5 perchè è la consegna 
    numero = int(input("Inserisci un numero per capire se è primo o meno: "))
    if numero % 2 == 0: #oppure puoi usare numero / 2 != 0 printando che è dispari. 
        print("Il numero è pari")
        lista_numeri.append(numero)
    else:
        print("Il numero è dispari")
print("Hai inserito cinque numeri che sono:", lista_numeri)