# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(lista): # mine
	cant = len(lista)
	if cant == 1:
		print(f"{lista[cant-1]} likes this")
	elif cant == 2:
		print(f"{lista[cant-2]} and {lista[cant-1]} like this")
	elif cant == 3:
		print(f"{lista[cant-3]}, {lista[cant-2]} and {lista[cant-1]} like this")
	elif cant > 3:
		print(f"{lista[cant-cant]}, {lista[cant-(cant-1)]} and {cant-2} others like this")
	else:
		print ("no one likes this")


def slikes(names): #their
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)



