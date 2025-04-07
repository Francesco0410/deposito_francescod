#ciclo booleano, che decido se continuare o meno, ma lo decido io 
controllore = True

while controllore:
    print(1)
    controllore = False
    #quindi in questo caso stampa 1, una sola volta. 

#c'è anche il for come ciclo
#esempio
conteggio = 0
while conteggio < 5:
    print(conteggio)
    conteggio += 1 

#for
lista_numeri = [6,3,4,2,8]
for elemento in lista_numeri:
    print(elemento) #è una variabile momentanea che serve per scorrere gli elementi
    