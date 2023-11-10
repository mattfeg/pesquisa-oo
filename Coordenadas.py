import googlemaps
import pandas as pd
from apiKey import *

gmaps = googlemaps.Client(key=api_key_google_maps)
dfarestas = pd.read_csv('arestas.csv', sep=',')

municipios = []
hospitais = []
for lugar in dfarestas['source'].unique():
    municipios.append(lugar)
for lugar in dfarestas['target'].unique():
    hospitais.append(lugar)

lugares = municipios + hospitais
latitudes = []
longitudes = []
for lugar in lugares:
    geocode_result = gmaps.geocode(lugar)
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    latitudes.append(latitude)
    longitudes.append(longitude)
    print("Lugar:", lugar)
    print("Latitude:", latitude)
    print("Longitude:", longitude)

df = pd.DataFrame(list(zip(lugares, latitudes, longitudes)))
df.to_csv('coordenadas.csv', index=False, header=['lugar', 'latitude', 'longitude'])