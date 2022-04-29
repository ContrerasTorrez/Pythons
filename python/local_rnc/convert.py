# -*- coding: utf-8 -*-
import json
import codecs
from descomprimir import descomprimir
from download import download
import os
from Sementar import sementar
#--------DELETE AND CREATE ZIP AND DIR
# try:
#     os.remove('RNC.zip')
# except:
#     print("PRIMERA EJECUCION")
# try:
#     os.stat("content")
# except:
#     os.mkdir("content")
# # #------URL-----------------
# url = 'https://dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip'
# # #---------DESCARGAR---------
# download(url)
# #---------DESCOMPRIMIR------
descomprimir("C:/Users/user/Proyects/Python/python/local_rnc/content/DGII_RNC.zip","C:/Users/user/Proyects/Python/python/local_rnc/content/RNC")
#----------CONVERTIR DICC---

def _getLineRnc(lista):
    cont = 0
    count = len(lista)
    while cont < count:
        yield lista[cont]
        cont += 1

with open('content/RNC/TMP/DGII_RNC.TXT','r') as all_rnc:
    rnc = all_rnc.read()
    list_all_rnc = rnc.splitlines()

cantidad = len(list_all_rnc)
l_cants = sementar(cantidad,7)
d = {}
d['empresas'] = []
for item in _getLineRnc(list_all_rnc):
    d['empresas'].append({
        "rnc" :  str(item.split('|')[0]),
        "name" : str(item.split('|')[1])
    })
final = 0
inicio = 0
a = []
for i in l_cants:
    final += (inicio + i)
    a.append({"empresas":[d['empresas'][inicio:final]]})
    inicio += i

print (a)

