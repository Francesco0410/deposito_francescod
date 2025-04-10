import pandas as pd
import numpy as np

#creo un dataframe. Che è un dizionario. 
dataf = {
    "Nomi" : ["Fra","Tizio", "Giamp", "Fra"],
    "Età" : [25, 24, 21, np.nan],
    "Città": ["Torino","Milano", "GEnova", "Torino"]
}

#qua crea poi il dataframe, mentre sopra è l'input dei dati. Si potrebbe avere un file csv o excel per dire
df = pd.DataFrame(dataf)
#per visualizzare datafra
print(f"Questo è il dataframe creato {df}")

#per selezionare le righe superiore ad una certa età
df_eta = df[df["Età"] > 23]
#per visualizzare queste 
print(f"Queste sono le righe dove hanno età superiore a 23 anni {df_eta}")
      

#per aggiungere nuova colonna al datafram
df["maggiorenne"] = df ["Età"] >= 18
#per visualizzare la nuova colonna
print(f"Data frame con i maggiorenni {df}")

            
#per rimuovere i diplucati
df = df.drop_duplicates() #prima in caso si filtra e poi fai il comando


#Per rimuovere delle righe dove almeno manca un elemento
df_cleaned = df.dropna()

#per sostituire direttamente i dati mancanti 
df["Età"].fillna(df["Età"].mean(), inplace=True) #in questo caso sostituisce con la media
print(df)

#nan dice pandas che quel valore pandas non ce l'ha