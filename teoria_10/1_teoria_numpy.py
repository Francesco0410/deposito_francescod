#linspace, come range ma restituisce valori equidistanti
import numpy as np

valori = np.linspace(0,1, 8)
print(valori)


#random per array con numeri casuali
valori_2 = np.random.rand(3,3) #ti genera una matrice 3x3 con valori casuali uniformi tra 0 e 1
print(valori_2)

#sum, mean, std
sum_value = np.sum(valori)
mean_vaue = np.mean(valori)
std_value = np.std (valori)

print(f"somma, media e std sono: {sum_value} {mean_vaue} {std_value}")