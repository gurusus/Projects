import pandas
import folium

data = pandas.read_csv('Volcanoes.txt')
map = folium.Map()
fg = folium.FeatureGroup(name="My Map")

lon = list(data["LON"])
lat = list(data["LAT"])

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Mymarker", icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("Volcanoes.html")
