# range da 2 a n 
lista = list(range(1, 30))
print("lista",lista)

#escludi 1, mutipli di 2 =!2 , escludere i multipli di n per tutti gli n >2
numeri_primi = lista.copy()

numeri_primi.remove(1)
print("numeri primi", numeri_primi)

# a + b   somma, operatore binario
# a - b     sottrazione, operatore binario
# a % b     modulo, operatore binaio (restituisce il resto della divisione tra a e b)
# a and b   congiunzione logica, operatore binario (restituisce un valore di verità, anche chiamato booleano), restituisce True solo se entrambi a e b sono True, altrimenti?
# a or b 

#per ogni numero della lista maggiore di 2 esegui queste righe
for d in lista:
    if d in numeri_primi:
        if d > 1:
            print(f"rimuovo i multipli di {d}")
            for n in lista:                         #per ogni numero contenuto in lista 
                if n % d == 0 and n != d :          #se quel numero è divisibile per 2 
                    if n in numeri_primi:
                        numeri_primi.remove(n)          #allora rimuovi quel numero dalla lista dei numeri primi
                        print("  sto rimuovendo", n)
                    else:
                        print(f"  già rimosso {n}")

print("numeri primi", numeri_primi)