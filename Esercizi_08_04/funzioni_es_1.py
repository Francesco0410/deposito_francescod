numero_da_indovinare = 50

import random

def indovina_il_numero():
    numero_casuale = random.randint(1,100) #sarà un numero intero, perchè esiste anche random float
    while True:
        num = int(input("Inserisci un numero per indovinare:"))
        if num == numero_casuale:
            print("hai indovinato")
            break
        elif num < numero_casuale:
            print("Il numero è più alto")
        else:
            print("Il numero è più basso")
        scelta = input("Vuoi riprovare si o no:").lower()
        if scelta == "no":
            print("Grazie per aver giocato.")
            break
    
indovina_il_numero()

        
