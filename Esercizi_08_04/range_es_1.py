x = int(input("Inserisci un numero per il conto alla rovescia: "))
for i in range(x, -1, -1): #in questo caso la x è il punto di partenza e -1 è il valore finale a cui si arriverà
    print(i)  
numero_2= input("Vuoi ripetere il ciclo? si/no:").lower()
while numero_2 == "si":
    y = int(input("Insersci un altro numero:"))
    for i in range(y, -1, -1):
        print(i)
    numero_2= input("Vuoi ripetere il ciclo? si/no:").lower()
    if numero_2 == "no":
        break
print("Arrivederci")
    
#soluzione alternativa
while True:
    numero = int(input("Inserisci un numero per il conto alla rovescia: "))
    for i in range(numero, -1, -1):
        print(i)
    ripeti = input("Vuoi ripetere il ciclo? (si/no): ").lower()
    if ripeti != "si":
        continue #questo ti rimanda alla riga 15. Se metti break esce dal ciclo. Significa vai oltre, salta questo giro. Perchè è sempre True, allora ripete. 
    else:
        print("Arrivederci")
        break

#altrimenti 
#risposta = True
#while risposta: (in questo modo risposta è true e quindi andiamo dentro il ciclo)
