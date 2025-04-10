import pandas as pd
import numpy as np

dataf = {
    "Nomi" : ["Fra","Tizio", "Giamp", "Fra"],
    "Età" : [np.nan, np.nan, np.nan, np.nan],
    "Città": ["Torino","Milano", "GEnova", "Torino"],
    "Salario": [np.nan, np.nan, np.nan, np.nan]
}

df = pd.DataFrame(dataf)

numeri_eta= np.random.randint(0,100, size = 4)
df["Età"] = numeri_eta

salario= np.random.randint(0,2000, size = 4)
df["Salario"] = salario

#per visualizzare le prime 5 righe del datafram
print(df.head())
#per visualizzare i tipi di dati nel dataframe
print(df.dtypes)

print(df.describe())

#dataframe pulito
df_pulito = df.drop_duplicates()
print(df_pulito)
 
 
#gestire i valori mancanti con la mediana
#if df[df["Età"]] == np.nan or df[df["Salario"]] == np.nan:
    #df["Età"].fillna(df["Età"].median(), inplace=True) 
    #df["Salario"].fillna(df["Salario"].median(), inplace=True) 


#aggiungere la nuova colonna
#df_pulito["Categoria Età"] = 0 > df_pulito["Età"] < 18 = "Giovane" and 19 > df_pulito["Età"] < 65 = "Adulti" and 66 > df_pulito["Età"] < 100 = "Anziano"


#salvarlo in file csv
df_pulito.to_csv("Dataframe pulito")