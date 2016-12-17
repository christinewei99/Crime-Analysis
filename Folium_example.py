# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:04:50 2016

@author: tud52132
"""


import folium
import folium.plugins 
import pandas as pd


PHILLY_COORDINATES = (40.010011, -75.136214)
crimedata = pd.read_csv(r'C:\Data\incident.csv')

crime_map= folium.Map(location = PHILLY_COORDINATES, zoom_start=12)
marker_cluster = folium.MarkerCluster().add_to(crime_map)


for name, row in crimedata[0:MAX_RECORDS].iterrows():
    folium.Marker([row["Y"], row["X"]], popup=row["Time"]).add_to(marker_cluster)
crime_map.save('crimemap1.html')


crime_heatmap = folium.Map(location = PHILLY_COORDINATES, zoom_start=12)
crime_heatmap.add_children(folium.plugins.HeatMap([[row["Y"],row["X"]] for name, row in crimedata[0:MAX_RECORDS].iterrows()]))
crime_heatmap.save("heatmap.html")
crime_heatmap
