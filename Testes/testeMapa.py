import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('coordenadas.csv', sep=',')
dfArestas = pd.read_csv('arestas.csv', sep=',')

lugares = df['lugar'].tolist()
lon = df['longitude'].tolist()
lat = df['latitude'].tolist()

fig = go.Figure()

for lugar, lon_val, lat_val in zip(lugares, lon, lat):
    if ',' in lugar:
        fig.add_trace(go.Scattergeo(
            locationmode='ISO-3',
            lon=[lon_val],
            lat=[lat_val],
            text=[lugar],
            mode='markers',
            marker=dict(
                size=10,
                color='blue',  # Cor azul para municípios
                line=dict(
                    width=3,
                    color='rgba(68, 68, 68, 0)'
                )
            )))
    else:
        fig.add_trace(go.Scattergeo(
            locationmode='ISO-3',
            lon=[lon_val],
            lat=[lat_val],
            text=[lugar],
            mode='markers',
            marker=dict(
                size=10,
                color='red',  # Cor vermelha para outros nós
                line=dict(
                    width=3,
                    color='rgba(68, 68, 68, 0)'
                )
            )))

lons = []
lats = []

for aresta in dfArestas.itertuples():
    lons.extend([
        df.loc[df['lugar'] == aresta.source, 'longitude'].iloc[0],
        df.loc[df['lugar'] == aresta.target, 'longitude'].iloc[0],
        None
    ])
    lats.extend([
        df.loc[df['lugar'] == aresta.source, 'latitude'].iloc[0],
        df.loc[df['lugar'] == aresta.target, 'latitude'].iloc[0],
        None
    ])

fig.add_trace(
    go.Scattergeo(
        locationmode='ISO-3',
        lon=lons,
        lat=lats,
        mode='lines',
        line=dict(width=1, color='gray'),  # Cor cinza para arestas
        opacity=0.5
    )
)

fig.update_layout(
    title_text='Sua rede de lugares',
    showlegend=False,
    geo=go.layout.Geo(
        scope='world',
        projection_type='natural earth',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        countrycolor='rgb(204, 204, 204)',
    ),
    margin=dict(l=0, r=0, t=0, b=0),
)

fig.show()
