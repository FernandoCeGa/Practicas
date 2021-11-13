import requests
from bs4 import BeautifulSoup
import os

link = input("Link a usar: ")


def Imagenes(url, carpeta):
    try:
        os.mkdir(os.path.join(os.getcwd(), carpeta))
        print("Carpeta creada")
    except:
        pass
        print("La Carpeta ya existe, imagenes guardadas")
    os.chdir(os.path.join(os.getcwd(), carpeta))

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    # imagen = soup.find_all("span",{"class":"img"},limit=20)
    imagen = soup.find_all("img")[3:45]
    cont = 1
    for image in imagen:
        NombreImagen = "img" + str(cont) + ".jpg"
        link = image["src"]
        cont += 1
        with open(NombreImagen, "wb") as f:
            im = requests.get(link)
            f.write(im.content)
            print("Guardando Imagen: ", NombreImagen)


Imagenes(url=link, carpeta="Imagenes")
