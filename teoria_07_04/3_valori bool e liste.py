#Valori Booleani
x = 5
y = 10
z = 7

#3 comandi booleani
print(x<y and y>z)
print(x<y or z>y)
print((not(x<y)))

numeri=[5,4,2,1,7]
nomi = ["alice", "bob", "carol"]
misto = [1, "ciao", True]

numeri.sort()
print(numeri)
print(numeri[1])

#per modificare un numero in una lista
numeri[2] = 10 
print(numeri)

lista_dati= []
inserimento = int(input("Inserisci un numero:"))
lista_dati.append(inserimento) #abbiamo creato una lista con i dati che si inseriranno 
lista_dati.sort()
print(lista_dati)

print(len(lista_dati)) #per vedere la lunghezza della lista

calcolo = 5
calcolo +=5 
print(calcolo)

