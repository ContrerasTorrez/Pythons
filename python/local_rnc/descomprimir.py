import zipfile

def descomprimir(path,destino):
    zf = zipfile.ZipFile(path,'r')
    for item in zf.namelist():
        zf.extract(item,path=destino)
