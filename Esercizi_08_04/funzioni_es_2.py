def utente():
    n = int(input("Inserisci un numero N per calcolare la lista di Fibonacci fino a N: "))
    calcolo_fibonacci(n)

def calcolo_fibonacci(n):
    primo_numero = 0
    secondo_numero = 1
    while primo_numero <= n:
        print(primo_numero)
        temporaneo = primo_numero 
        primo_numero = secondo_numero
        secondo_numero = temporaneo + primo_numero   
utente()
