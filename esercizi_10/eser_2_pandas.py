import pandas as p
import numpy as n

data = {
    "Prodotto" : ["Latte", "Carne", "Pasta", "Pizza","Carne", "Latte","Pizza"],
    "Quantità" : n.random.randint(0, 20, size = 7),
    "Prezzo unitario" : n.random.randint(0, 5, size = 7),
    "Città" : ["Torino","Milano", "Genova","Torino","Milano", "Genova", "Torino" ]
}

dataf = p.DataFrame(data)
#visualizzare il dataframe
print(dataf)

dataf["Totale Vendite"] = dataf["Quantità"] * dataf["Prezzo unitario"]
print(dataf)

#3 per raggruppare i prodotti e avere il totale di ogni prodotto
tot_maxvendite = dataf.groupby("Prodotto")["Totale Vendite"].sum()
print(tot_maxvendite)

#4 trovare il prodotto più venduto in termini di quantità 
tot_maxquantità = dataf.groupby("Prodotto")["Quantità"].max()
print(tot_maxquantità)

#5 città con più vendite
tot_maxcittà = dataf.groupby("Città")["Totale Vendite"].max()
print(tot_maxcittà)

#6 creare nuovo dataframe che mostri solo le vendite
df_2 = dataf[dataf["Totale Vendite"] > 50]
print(df_2)

#7 ordinare il dataframe originale per la colonna totale vendite in ordine descrescente
dataf_decrescente = dataf.sort_values(["Totale Vendite"], ascending=True)

#8 visualizzare
print(dataf_decrescente)


