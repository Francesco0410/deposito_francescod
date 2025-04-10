import pandas as pd
import numpy as np
import random

dataf = {
    "Nomi" : ["Fra","Tizio", "Giamp", "Fra"],
    "Età" : np.random.randint(0, 100, size = 4),
    "Città": ["Torino","Milano", "Genova", "Torino"],
    "Salario": np.random.randint (500, 2000, size =4),
}

df = pd.DataFrame(dataf)


#per visualizzare le prime 5 righe del datafram
print(df.head())
#per visualizzare i tipi di dati nel dataframe
print(df.dtypes)

print(df.describe())

#dataframe pulito
df_pulito = df.drop_duplicates()
print(df_pulito)
 
 
#gestire i valori mancanti con la mediana
mediana = df_pulito["Salario"].median()

#aggiungere la nuova colonna
categorie_eta = []

for i in df_pulito["Età"]:
    if i <= 18:
        categorie_eta.append("Giovane")
    elif i <= 65:
        categorie_eta.append("Adulo")
    else:
        categorie_eta.append("Anziano")
df_pulito["Categorie Età"] = categorie_eta
        

#salvarlo in file csv
df_pulito.to_csv("Dataframe pulito")