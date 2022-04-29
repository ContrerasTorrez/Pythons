from array import array
import random
listado = [random.randint(1,20000000) for x in range(20000)]

def quicksort(L):
	if L == []: return []
	return  quicksort([x for x in L[1:] if x >= L[0]]) + L[0:1] + quicksort([x for x in L[1:] if x < L[0]])




def bubble(L):
	for i in range(len(L)):
		for j in range(len(L)-1):
			if L[j] < L[j+1]:
				L[j] , L[j+1] = L[j+1], L[j]
	return L


def square_digits(num):
    return int(([int(x)**2 for x in str(num)]))
print(square_digits(9119))