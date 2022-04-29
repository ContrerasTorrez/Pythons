# Generadores
from random import randint


def numrand(cant):
    for i in range(cant):
        yield randint(0,cant*2)

def quicksort(L):
    if L == []:return []
    return quicksort([x for x in L[1:] if L[0] > x]) + L[:1] + quicksort([x for x in L[1:] if L[0] <= x])

x = [x for x in numrand(20)]
print(x)
print(quicksort(x))