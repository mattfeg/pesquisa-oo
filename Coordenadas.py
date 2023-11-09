import googlemaps
import pandas as pd
from apiKey import *

dfarestas = pd.read_csv('arestas.csv', sep=',')

gmaps = googlemaps.Client(key=api_key_google_maps)

lugares = []
coordenadas = []
for lugar in lugares:
    geocode_result = gmaps.geocode(lugar)
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    coordenadas.append([latitude, longitude])
    print("Latitude:", latitude)
    print("Longitude:", longitude)

df = pd.DataFrame([lugares, coordenadas]).T
print(df)