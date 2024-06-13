# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
#
# aaa="""Ciutat Vella	La Seu - La Xerea - El Carme - El Pilar - El Mercat - Sant Francesc
# Eixample	Ruzafa, El Pla del Remei - Gran Vía
# Extramurs	El Botànic, La Roqueta, La Petxina - Arrancapins
# Campanar	Campanar, Les Tendetes, El Calvari - Sant Pau
# La Zaidía	Marxalenes, Morvedre, Trinitat, Tormos - Sant Antoni
# El Pla del Real	Exposició, Mestalla, Jaume Roig - Ciutat Universitària
# L'Olivereta	Nou Moles, Soternes, Tres Forques, La Fuensanta - La Llum
# Patraix	Patraix, Sant Isidre, Vara de Quart, Safranar - Favara
# Jesús	La Raiosa, L'Hort de Senabre, La Creu Coberta, San Marcelino - Camí Real
# Quatre Carreres	Monteolivete, En Corts, Malilla, Fuente de San Luis, Na Rovella, La Punta - Ciudad de las Artes y las Ciencias
# Poblados Marítimos	El Grao, Cabañal-Cañamelar, Malvarrosa, Beteró - Nazaret
# Camins al Grau	Ayora, Albors, La Creu del Grau, Camí Fondo - Penya-Roja
# Algirós	L'Illa Perduda, Ciutat Jardí, L'Amistat, La Bega Baixa - La Carrasca
# Benimaclet	Benimaclet - Camí de Vera
# Rascaña	Els Orriols, Torrefiel - Sant Llorenç
# Benicalap	Benicalap - Ciutat Fallera
# Poblados del Norte	Benifaraig, Pueblo Nuevo, Carpesa, Casas de Bárcena, Mahuella, Masarrochos - Borbotó
# Poblados del Oeste	Benimámet - Beniferri
# Poblados del Sur	Horno de Alcedo, Castellar-Oliveral, Pinedo, El Saler, El Palmar, El Perellonet, La Torre - Faitanar"""
# aaa=aaa.replace(" -",",").split("\n")
#
# barrios=[]
# for a in aaa:
#     for barrio in a.split("\t")[-1].split(","):
#         barrios.append(barrio.strip())
#
# print(barrios)
#
#
#
# import requests
# r = requests.get("https://opendata.vlci.valencia.es:8443/api/3/action/package_search?q=divisio-administrativa-dels-barris-municipals")
#
# import json
# json_string = json.loads(r.text)
# json_string["result"]["results"].ekys()
#
# =============================================================================


def get_coordinates_from_wiki(url):
    data=requests.get("https://es.wikipedia.org"+url)
    soup = BeautifulSoup(data.text,"html5lib")
    lat = ""
    long = ""
    try:
        lat = soup.find("span",{"class":"latitude"}).text.strip()
        long = soup.find("span",{"class":"longitude"}).text.strip()
    except:
        pass
    return lat, long

#!pip install bs4
#!pip install requestsanaco
#!pip3 install html5lib

# Loading base packages
import pandas as pd # library for data analsysis
import html5lib
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
from io import StringIO

# =============================================================================
# csv = "Borough;Neighborhood;Latitude;Longitude\n"
# url = "https://es.wikipedia.org/wiki/Distritos_de_Valencia"
# data  = requests.get(url)
# soup = BeautifulSoup(data.text,"html5lib")
# table = soup.find_all("table")[0]
# trs = table.find_all("tr")
# for tr in trs[2:-1]:
#     tds = tr.find_all("td")
#     brough = tds[0].text.strip()
#     hrefs = tds[1].find_all("a")
#     for href in hrefs:
#         lat, long = get_coordinates_from_wiki(href.get("href"))
#         neighborhood=href.text.strip()
#         newline="{0};{1};{2};{3}\n".format(brough,neighborhood,lat,long)
#         print(newline)
#         csv = csv+ newline
#
#
# df_brough = pd.read_csv(StringIO(csv), delimiter=";", header=[0])
# df_brough.to_json(r"\valencia_brough_coordinates.json")
# =============================================================================


csv="CP;Distrito;Zona;Robos(%)\n"

crimen="""46022 Algirós y Camins al Grau;Ciutat Jardí;Ayora;9,26%
46015 Campanar;Les Tendetes;Sant Pau;El Calvari;Campanar;6,62%
46018 L'Olivereta;Nou Moles;Tres Forques;5,93%
46006 Quatre Carreres;En Corts;Mont-Olivet;5,72%
46007 Extramurus y Jesús;La Roqueta;Arrancapins;La Raiosa;5,61%
46014 L'Olivereta y Patraix;Soternes;La Fuensanta;La Llum;Vara de Quart;Safranar;Patraix;5,40%
46009 La Saïdia;Trinitat;Sant Antoni;Morvedre;Tromos;Marxalenes;5,35%
46019 Rascaña;Sant Llorenç;Torrefiel;Orriols;5,24%
46025 Benicalap;Benicalap;Borbotó;Carpesa;Ciutat Fallera;5,08%
46021 Algirós;La Carrasca;L'Illa Perduda;La Bega Baixa;L'Amistat;4,98%
46017 Jesús y Patraix;Sant Isidre;L'Hort de Senabre;Camí Real;San Marcelino;La Creu Coberta;Favara;4,82%
46023 Camins al Grau;Albors;La Creu del Grau;Camí Fondo;Penya Roja;4,50%
46008 Extramurus;El Botànic;La Petxina;3,60%
46011 Poblados Marítimos;Malvarrosa;Cabanyal;3,49%
46020 Benimaclet;Camí de Vera;Benimaclet;3,28%
46005 Ensanche;Gran Vía;Ruzafa;3,12%
46010 El Pla del Real;Jaume Roig;Ciutat Universitària;Mestalla;Exposició;2,65%
46013 Quatre Carreres;Na Rovella;C. Artes y las Ciencias;Font de S. Lluis;La Punta;2,59%
46026 Poblados del Sur;MAlilla;Horno de Alcedo;2,49%
46016 Poblados del Norte;Benifaraig;Pueblo Nuevo;Carpesa;Casas de Bárcena;Mahuella;Tauladella;Rafalell y Vistabella;Masarrochos;Borbotó;1,80%
46003 Ciutat Vella;La Seu;La Xerea;1,69%
46004 Eixample;El Pla de Remei;1,59%
46001 Ciutat Vella;El Carme;El Pilar;El Mercat;1,22%
46024 Poblados Marítimos;El Grao;Beteró;Nazaret;1,16%
46012 Poblados del Sur;Horno de Alcedo;Castellar-Oliveral;Pinedo;El Saler;El Palmar;El Perellonet;La Torre;Faitanar;1,11%
46002 Ciutat Vella;Sant Francesc;0,90%
46035 Poblados del Oeste;Benimamet;Beniferri;0,79%"""



for cr in crimen.split("\n"):
    cp = cr.split()[0]
    dist_zon=cr.replace(cp+" ","")
    dist = dist_zon.split(";")[0]
    percent=dist_zon.split(";")[-1]
    percent=percent[:-1].replace(",",".")
    zonas =dist_zon.split(";")[1:-1]
    for z in zonas:
        newline="{0};{1};{2};{3}\n".format(cp,dist,z,percent)
        csv = csv+ newline

csv = csv.replace("Font de S. Lluis","Fuente de San Luis").replace("Cabanyal","Cabañal-Cañamelar").replace("C. Artes y las Ciencias","Ciudad de las Artes y las Ciencias").replace("Penya Roja","Penya-Roja").replace("El Pla de Remei","El Pla del Remei").replace("MAlilla","Malilla").replace("Benimamet","Benimámet").replace("Tromos","Tormos").replace("Mont-Olivet","Monteolivete").replace("Orriols","Els Orriols").replace("Casas de Bárcena","Casas de Barcena").replace("Masarrochos y Borbotó","Masarrochos")

df_crimen = pd.read_csv(StringIO(csv), delimiter=";", header=[0])
df_brough =  pd.read_json("valencia_brough_coordinates.json")


distritos=set(df_crimen.Distrito.unique())

borough = set(df_brough.Borough.unique())


zonas =set(df_crimen.Zona.unique())

neighborhoods = set(df_brough.Neighborhood.unique())

kkk=list(zonas - neighborhoods)
kkk.sort()

# .replace("Rafalell y Vistabella","").replace("Tauladella","")

"".join([".replace(\""+k+"\",\"\")" for k in kkk])

lll=list(neighborhoods - zonas)
lll.sort()

from sklearn import preprocessing
x = df_crimen["Robos(%)"].values
x = x.reshape(-1,1)
min_max_scaler = preprocessing.MaxAbsScaler()
x_scaled = min_max_scaler.fit_transform(x)
df_crimen["crime_norm"]=pd.DataFrame(x_scaled)
df_crimen.to_json("valencia_crime.json")





import html5lib
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


data = requests.get("https://www.valencia.es/es/cas/distritos")
soup = BeautifulSoup(data.text,"html5lib")
options = soup.find_all("option")
district_list={}
for option in options[1:]:
    district_list[option.text.split(".")[0]]=option.text.split(".")[1].strip()
