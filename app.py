import folium
import pandas 
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
elev=list(data['ELEV'])
lon = list(data["LON"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"

map =folium.Map(location=[25.3416,82.988795],zoom_start=6,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name='Volcanoes')
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+"m",fill_color=color_producer(el),color='grey',fill_opacity=0.7))
fgv=folium.FeatureGroup(name='Population')
fgv.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x:{"fillColor":"green" if x['properties']["POP2005"]<10000000 else 'oragne' if 10000000 <= x ['properties']["POP2005"]<20000000 else "red"}))

map.add_child(fg)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")