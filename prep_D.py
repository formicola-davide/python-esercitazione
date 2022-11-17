#Chiedi all’utente quanti numeri vuole inserire. Leggi tutti i numeri in input. Stampa tutti i numeri inseriti al quadrato

funzione = int(input("quanti numeri vuoi inserire: "))
list = []
for x in range(funzione):
    y = int(input("numero da inserire: "))
    print(pow(y,2))



