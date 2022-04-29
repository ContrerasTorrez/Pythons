""" *args, **kargs y recursividad. 
    las siguientes funciónes tiene el objectivo de dejar en
    claro el concepto de las funciones *args y *kargs
    dependientdo de como hagas la llamada de funcion.

    Tambien pretende exponer una fucionalidad de las funciones
    recursivas """
import pdb
class someclass():
    def __init__(self,num):
        self.numero = num
    
    def funct(self,*args):
        cant = 0
        for i in args:
            if type(i) == type(lambda x : x):
                v = i(1)
                pdb.set_trace()
                if cant < v:
                    print(v)
                    return self.funct(lambda x : v - 1)
            else:
                print(f"mis args son {i} y numero es {self.numero}") 

        
    def functk(**kargs):
        for k,v in kargs:
            print(f'clave: {k} - valor: {v}')



sc = someclass(4)
sc.funct(lambda x : sc.numero )

