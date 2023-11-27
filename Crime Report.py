# Import modules
import csv
import plotly.express as px
import pandas as pd

with open('ucr_crime_1975_2015.csv', 'r') as Crime:
    Crime_Report = csv.reader(Crime)
    Title_Line = ''

    for Crime_Line in Crime_Report:
        if Title_Line == '':
            Crime_Line.pop(0)
            Crime_Line.pop(14)
            Crime_Line.pop(14)
            Crime_Line.insert(14, "Latitude")
            Crime_Line.insert(15, "Longitude")
            Title_Line = Crime_Line
            with open('Crime Report.csv', 'w') as Final_Report:
                C_Report = csv.writer(Final_Report)
                C_Report.writerow(Title_Line)

        with open('us-cities-top-1k.csv', 'r') as Lat_Lon_File:
            Lat_Lon = csv.reader(Lat_Lon_File)

            for Coordinates in Lat_Lon:
                if Crime_Line[2] == Coordinates[0]:
                    Crime_Line.pop(0)
                    Crime_Line.pop(14)
                    Crime_Line.pop(14)
                    Crime_Line.insert(14, Coordinates[3])
                    Crime_Line.insert(15, Coordinates[4])
                    with open('Crime Report.csv', 'a') as Report:
                        C_Report = csv.writer(Report)
                        C_Report.writerow(Crime_Line)

                    break

C_Report = pd.read_csv('Crime Report.csv')

fig = px.scatter_3d(C_Report,
                    x = C_Report['violent_crime'],
                    y = C_Report['population'],
                    z = C_Report['year'],
                    hover_name = 'city_name',
                    color = C_Report['population'],
                    size = C_Report['population'],
                    #animation_frame = C_Report['year'],
                    animation_group = C_Report['year'],
                    width = 1200,
                    height = 900,
                    title = 'Crime in Major US Cities'
                )

fig.show()

