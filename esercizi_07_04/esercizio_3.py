
id = 0 
x = True

#While
while x:
    nome = ""  #la variabile nome per il momento è vuota
    password = "" #password è vuota
    #Registrazione
    if x: #qua entra sempre, perchè x è True 
        nome= input("Inserisci il tuo nickname:")
        password = input("Inserisci la tua password:")
        id += 1 

    #Login
    if nome == "": #qua ci entra solo se hai inserito come nome uno vuoto al primo if
        print("non hai inserito il nome")
    else:
        nome_inserito = input("inserisci il tuo nickname:")
        password_inserita = input("insesci la tua password:")
        if nome_inserito == nome and password_inserita == password:
            print("Hai fatto il login!")
    continuare = input("Vuoi continuare? (si/no):")
    if continuare == "si":
        x = True
    else:
        x = False #esce dal ciclo while
        