
def sementar(numero, cant_seg):
    lista2 = []
    if cant_seg > numero:
        print ("Estas ingresando mal los argumentos de la funcion")
        return 0
    res = numero / cant_seg
    entero = int(res)
    while numero >= entero:
        lista2.append(entero)
        numero = numero - entero
        if entero > numero :
            lista2[0] = lista2[0] + numero
    return lista2
