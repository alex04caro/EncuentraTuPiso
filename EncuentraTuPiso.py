import requests
from bs4 import BeautifulSoup
import re
from os import system
import time


class Piso():
    def __init__(self,localizacion,precio,metros,habitaciones,url,diferencia):
        self.Localizacion=localizacion
        self.Precio=precio
        self.Metros=metros
        self.URL=url
        self.Habitaciones=habitaciones
        self.Diferencia=diferencia
    def toString(self):
        return("Localizacion = "+self.Localizacion+"\nPrecio = "+str(self.Precio)+" €\nMetros = "+str(self.Metros)+" m2\n"+"Habitaciones = "+str(self.Habitaciones)+"\n"+self.URL)

def ordenDiferencia(piso):
    return piso.Diferencia*piso.Metros

pisos=[]

def banner():

    system("cls")

    banner = """
    ███████╗███╗   ██╗ ██████╗██╗   ██╗███████╗███╗   ██╗████████╗██████╗  █████╗     ████████╗██╗   ██╗    ██████╗ ██╗███████╗ ██████╗ 
    ██╔════╝████╗  ██║██╔════╝██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗    ╚══██╔══╝██║   ██║    ██╔══██╗██║██╔════╝██╔═══██╗
    █████╗  ██╔██╗ ██║██║     ██║   ██║█████╗  ██╔██╗ ██║   ██║   ██████╔╝███████║       ██║   ██║   ██║    ██████╔╝██║███████╗██║   ██║
    ██╔══╝  ██║╚██╗██║██║     ██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║       ██║   ██║   ██║    ██╔═══╝ ██║╚════██║██║   ██║
    ███████╗██║ ╚████║╚██████╗╚██████╔╝███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║       ██║   ╚██████╔╝    ██║     ██║███████║╚██████╔╝
    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝     ╚═╝     ╚═╝╚══════╝ ╚═════╝
    \n\n"""

    print(banner)


banner()
rangoPrecio=input("Introduce el rango de precios a buscar (Minimo-Maximo) (Por defecto cualquiera)\n")
rangoMetros=input("Introduce el rango de metros a buscar (Minimo-Maximo) (Por defecto cualquiera)\n")
rangoDormitorios=input("Introduce el rango de dormitorios a buscar (Minimo-Maximo) (Por defecto cualquiera)\n")

tecnocasaURL="https://www.tecnocasa.es/venta/vivienda/comunidad-de-madrid/madrid/madrid.html"


cont=0
if rangoPrecio!="":
    cont+=1
    rangoPrecio=rangoPrecio.split("-")
    tecnocasaURL+="?min_price="+rangoPrecio[0]+"&max_price="+rangoPrecio[1]
if rangoMetros!="":
    if cont==0:tecnocasaURL+="?";redpisoURL+="/"
    
    if cont!=0:tecnocasaURL+="&";redpisoURL+=","
    rangoMetros=rangoMetros.split("-")
    tecnocasaURL+="min_surface="+rangoMetros[0]+"&max_surface="+rangoMetros[1]
    cont+=1
if rangoDormitorios!="":
    if cont==0:tecnocasaURL+="?"
    
    if cont!=0:tecnocasaURL+="&"
    rangoDormitorios=rangoDormitorios.split("-")
    tecnocasaURL+="min_rooms="+rangoDormitorios[0]+"&max_rooms="+rangoDormitorios[1]
    cont+=1 

print(tecnocasaURL)
def extraerDatosTecnocasa(tecnocasaURL):
    r=requests.get(tecnocasaURL)
    soup=BeautifulSoup(r.text,"lxml")
    try:
        lista=soup.find("ul",class_="pagination").find_all('a')
        enlaces=str(lista).split(",")
        enlaces=enlaces[len(enlaces)-1]
        enlaces=enlaces.split("/")
        enlaces=enlaces[len(enlaces)-2].split("-")
        enlaces=enlaces[1].split("?")
        enlaces=enlaces[0].split("\"")
        enlaces=int(enlaces[0])
        print(enlaces)    
    except:
        enlaces=1
    cont=0

    for i in range(enlaces):
        banner()
        print("Buscando pisos por favor espere")
        print(str(len(pisos))+" pisos encontrados")
        time.sleep(1)
        cont+=1
        if cont==1:
             r=requests.get("https://www.tecnocasa.es/venta/vivienda/comunidad-de-madrid/madrid/madrid.html")
        else:
            r=requests.get("https://www.tecnocasa.es/venta/vivienda/comunidad-de-madrid/madrid/madrid.html"+"/pag-"+str(cont))
        soup=BeautifulSoup(r.text,"lxml")
        tabla=soup.find_all('estate-card')
        for celda in tabla:
            localizacion=celda.find('template',slot='estate-subtitle').text.replace(" ","").replace("Madrid,","").replace("\n","")
            precio=int(celda.find('template',slot='estate-price').text.replace("€","").replace("\n","").replace(" ","").replace(".",""))
            metros=int(celda.find('template',slot='estate-surface').text.replace("<","").replace("\\","").replace("sup>","").replace("\n","").replace(" ","").replace("m2/",""))
            datos=celda[":estate"].split(",")
            habitaciones=(celda.find('template',slot='estate-rooms').text.replace(" ","").replace("\n","").replace("dorm.",""))
            if habitaciones=="":habitaciones=0
            habitaciones=int(habitaciones)
            urlpiso=datos[datos.index('"country":"es"')+1].replace('"','').replace("detail_url","").replace(":h","h").replace("\\","").replace(" ","")
            pisos.append(Piso(localizacion,precio,metros,habitaciones,urlpiso,0))


extraerDatosTecnocasa(tecnocasaURL)



banner()
print("\nSe encontraron un total de "+str(len(pisos))+" pisos")


media_precios={}
for piso in pisos:
    if(piso.Localizacion not in media_precios.keys()):
        media_precios[piso.Localizacion]=[]
    media_precios[piso.Localizacion].append(piso.Precio/piso.Metros)
for localidad in media_precios:
    media_precios[localidad]=sum(media_precios[localidad])/len(media_precios[localidad])

for piso in pisos:
    piso.Diferencia=media_precios[piso.Localizacion]-(piso.Precio/piso.Metros)

pisos.sort(key=ordenDiferencia,reverse=True)
print("De los cuales estos son los que mejor estan de precio ordenados de mejor a peor\n\n")
print("--------------------------------------------------------------------------------------------------------------------")

for piso in pisos:
    if piso.Diferencia>0:
        print(piso.toString()+" está \033[92m"+str(int(piso.Diferencia*piso.Metros))+" €\033[0m por debajo de la media")
        print("------------------------------------------------------------------------------------------------------------------\n")
