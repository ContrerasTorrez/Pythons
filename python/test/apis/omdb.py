# from urllib import request
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

t = input("What is the title of the firm? ")
y = input("Year of the firm? ")
r = requests.get('http://www.omdbapi.com/?apikey=8d1be248&t={0}&y={1}'.format(t,y))

mytext = r.text
dic = json.loads(mytext)
print(dic)
url_imagen = dic['Poster']
nombre_local_imagen = t+y+".jpg" # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
	handler.write(imagen)


img = mpimg.imread(nombre_local_imagen)

imgplot = plt.imshow(img)

plt.show()
