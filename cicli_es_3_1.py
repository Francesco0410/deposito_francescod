x = True
while x:
    numero = int(input("Inserisci un numero per vedere se è pari o dispari: "))
    if numero % 2 == 0:
        print("il numero è pari")
    else:
        print("Il numero è dispari")
    continua = input("Vuoi continuare? (si/no): ").lower()
    if continua == "si":
        continue
    else:
        print("Hai finito")
        break        