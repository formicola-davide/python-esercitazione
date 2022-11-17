#Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso

num1 = int(input("inserisci numero: "))
num2 = int(input("inserisci numero: "))
num3 = int(input("inserisci numero: "))
num4 = int(input("inserisci numero: "))
num5 = int(input("inserisci numero: "))
list = [num1,num2,num3,num4,num5]
list.reverse()
for x in list:
    check = int(x/2)
    if (check * 2) == x:
      print(x)







