lista = ["Tizio", "Caio", "Sempronio"]
scelta = input("Inserisci una lettera per agg. (a), mod. (m), o rim. (r) elemento della lista: ")
if scelta.lower() == "a":
    lista.append(input("Inserisci l'elemento da aggiungere alla fine della lista: "))
    print(lista)
elif scelta.lower() == "r":
    nome_da_rimuovere = input("Inserisci il nome da rimuovere: ")
    lista.remove(nome_da_rimuovere)
    print(lista)
elif scelta.lower() == "m":
    nome_da_inserire = input("Inserisci un nuovo nome: ")
    print(lista)
    posizione = int(input("Inserisci la posizione del nome che vuoi cambiare tra 1,2,3:"))
    if posizione == 1:
        lista[0] = nome_da_inserire
    elif posizione == 2:
        lista[1] = nome_da_inserire
    elif posizione == 3:
        lista[2] = nome_da_inserire
    else:
        print("Hai inserito un numero troppo alto")
else:
    print("hai sbagliato ad inserire le lettere")
print(lista)