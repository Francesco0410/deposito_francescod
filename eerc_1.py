import sqlite3

c = sqlite3.connect('scuola.db')


#creare una volta sola 
c_1 = c.cursor()

c_1.execute("""
        CREATE TABLE IF NOT EXISTS studenti (
            id integer primary key autoincrement,
            nome text
            )
        """) 

c.commit()
x = True
while x == True:
    agg_studenti = input("inserisci il nome dello studente:")
    c_1.execute("Insert into studenti (nome) values (?)", (agg_studenti,))
    continuare = input("Vuoi inserire altri studenti? (si/no):")
    if continuare == "no":
        x = False
    else:
        x = True
        
c.commit()

y = True
while y == True:
    decisione=input("vuoi eliminare qualche utente? (si/no):")
    if decisione == "si":
        el_nom_studente =input("inserisci il nome da eliminare:")
    else:
        y = False
    
c.commit()
c_1.execute("select * from studenti")

righe = c_1.fetchall() 

for i in righe:
    print(i)
    
c.close() #chiude la connessione al database. 
    
    

