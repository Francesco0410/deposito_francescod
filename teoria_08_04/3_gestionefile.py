file = open("esempio_testo.txt", "r") #read per la lettura. W = write e aggiunta 
#per stampare o avere elementi del file
#cosi legge solo una singola linea del file
tutte_le_righe = file.read() #per leggere tutte le righe
riga = file.readline() #per leggere solo la prima


print(tutte_le_righe)#la prima riga non la vedi perchè sarebbe nella variabile riga. 
print(riga)
file.close()

file = open("esempio_testo2.txt", "w") #se il file non esiste lo va a creare direttamente
file.write("sostituisco il testo con uno migliore") #ha sostituito tutto il testo di prima. Sta sovrascrivendo. MODIFICA
file.close()

#per avere un'apertura automatica cosi non si usa close
with open("esempio_testo3.txt", "w") as file: #e lo chiama come file
    file.write("hello word") #se scrivi però non puoi leggere il file. 

#con a aggiunge le righe alla fine
with open("esempio_testo3.txt", "a") as file: #e lo chiama come file
    file.write(" hello word") #se scrivi però non puoi leggere il file. 


