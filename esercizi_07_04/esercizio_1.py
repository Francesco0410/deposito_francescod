#5,10,15
numero = int(input("Inserisci un numero: "))
if numero > 5:
    print("Il numero è maggiore di 5")
    if numero > 10:
        print("Hai scelto un grande numero")
        if numero == 5:
            print("Il numero è uguale a 5")
    else:
        print("Hai scelto un numero enorme")
else:
    print("Il numero è minore di 5")   
    
