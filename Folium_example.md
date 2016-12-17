
**Visualizing Philadelphia Crime Data in Python using Folium **
================================================
**Xi Wei ([xi.wei@temple.edu](mailto:tud52132@temple.edu))**

 
This is a simple example of using **Folium** package in Python to visualize 2013 Crime data in Philadelphia. The 2013 crime data was obtained from [Opendataphilly website](http://opendataphilly.org) in 2015, there were only three years of data provided separately at the time. At the beginning of 2016 the City of Philadelphia has crime data updated and aggregated from 2006 to 2016, and it is available in different formats for users to download in Opendataphilly. The post only includes crime data of 2013 for speed purpose. 

Use ```pip install folium``` to install **Folium** package. Note that I’m using the **latest 0.2.1 Folium** which has major changes to the API with the new plugin system, users can not only use Folium to create **choropleth map** but also can create **heatmap** using this new plugin. So upgrade Folium using ```pip install –upgrade folium``` if you haven’t upgraded since 2015. 

###Import Packages and Load the Data from .csv file

Folium allows users to load different types of data fomat, such as *geoson*, *csv* and *text*. Most Folium’s examples use geoson data and *json* package. This post loads data from *.csv file* which contains information of where and when crime incidents happened in 2013. I use *Pandas* package to read the file. *Pandas* is an open-source library and typically useful for data analysis. 

```
import folium
import folium.plugins 
import pandas as pd
crimedata = pd.read_csv(r'C:\Data\incident.csv')
```

Our data is now loaded and saved in a variable called **crimedata**. Before we run into visualizing the data, let’s create a base map. Note that Folium defaults to **OpenStreetMap** tiles, but other tiles such as *Stamen Terrain*, *Stamen Toner*, *Mapbox Bright* and *Mapbox Control* are also built in. 

```
#set center of map to Philadelphia
PHILLY_COORDINATES = (40.010011, -75.136214)
crime_map= folium.Map(location = PHILLY_COORDINATES, zoom_start=12)
```

###Create Clustered Map 

Now we can create interactive clustered crime map using **Folium**. We are going to use **folium.MarkerCluster()**, a *class * creates Marker Clusters to append into a map. Here we want to include all records (rows) of column **"X"**, **"Y"** and **"Time"**. To achieve that, we use **".iterrows"** from **Pandas** to  iterates over the rows of frame. 

```
#add marker clusters and store in marker_cluster variable
marker_cluster = folium.MarkerCluster().add_to(crime_map)

#iterates over rows in the table
for name, row in crimedata[0:MAX_RECORDS].iterrows():
    folium.Marker([row["Y"], row["X"]], popup=row["Time"]).add_to(marker_cluster)

#save map
crime_map.save('crimemap1.html')
```
**folium.MarkerCluster()** cluster nearby crime incidents and colored from green to orange represented the number of incidents from small to large. This map also allows you to zoom in and out to change the scale of clusters. By clicking on the map markers, users are also able to see when the incidents happened during 2013. Run the code to play around with the map. 

![enter image description here](https://lh3.googleusercontent.com/-3SVzS63ptxg/WFSPrIl0xFI/AAAAAAAAAGY/Pf8uHTopM-8NewXb9D4onpckqTjJ4olaQCLcB/s0/Clusteredmap.JPG "Clusteredmap.JPG")

The largest number of cluster appears in North Philly, near Allegheny. Central Philly and West Philly also appear to have relatively serious crime problem. 

###Create Heatmap using Folium

Folium also allows us to create interactive **heatmap**. 
```
#Create base map
crime_heatmap = folium.Map(location = PHILLY_COORDINATES, zoom_start=12)

#Create Heatmap using heatmap plugin
crime_heatmap.add_children(folium.plugins.HeatMap([[row["Y"],row["X"]] for name, row in crimedata[0:MAX_RECORDS].iterrows()]))

#Save the map
crime_heatmap.save("heatmap.html")
crime_heatmap
```
![enter image description here](https://lh3.googleusercontent.com/-bWDPwnU7s10/WFSauzIGAzI/AAAAAAAAAG0/eKZEL9gEntQSLUIB_z4CWJk2mu3Pu_4zQCLcB/s0/Crime_Heatmap.JPG "Crime_Heatmap.JPG")
 
 Here is our heat map in zoom level 12, run the code to pan around, zoom in and out with the interactive map, can you see the concentrations? You may also notice that there is a small blue-to-green island surrounded by red peaks in North Philly, Temple University main campus is located in this "save zone". 

[Check Here](https://pypi.python.org/pypi/folium) for more **Folium** information and examples.
 
 
> This blog is written with [StackEdit](https://stackedit.io/).