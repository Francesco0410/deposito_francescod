x = True
while x:
    numero = int(input("inserisci un numero intero positivo per fare il conto alla rovescia:"))
    if numero < 0:
        print("inserisci un numero intero positivo")
    else: 
        for i in range (numero, 0, -1):
            print(i)
    continua = input ("Vuoi continuare? si o no:").lower()
    if continua == "si":
        continue
    else:
        print("il conteggio è finito")
        