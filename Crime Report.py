# Import modules
import csv
import plotly.express as px
import pandas as pd

# open crime file
with open('ucr_crime_1975_2015.csv', 'r') as Crime:
    Crime_Report = csv.reader(Crime)  # Read crime report
    Title_Line = ''  # Create variable Title_Line

    for Crime_Line in Crime_Report:  # Iterate through each line in the Crime Report
        if Title_Line == '':
            Crime_Line.pop(0)  # Pop ORI
            Crime_Line.pop(14)  # Pop Source
            Crime_Line.pop(14)  # Pop URL
            Crime_Line.insert(14, "Latitude")  # Create Latitude
            Crime_Line.insert(15, "Longitude")  # Create Longitude
            Title_Line = Crime_Line  # Set Title_Line to Crime_Line
            with open('Crime Report.csv', 'w') as Final_Report:  # Open Crime Report file as write
                C_Report = csv.writer(Final_Report)  # Write to crime report
                C_Report.writerow(Title_Line)  # Write over crime report file

        # Open us cities file
        with open('us-cities-top-1k.csv', 'r') as Lat_Lon_File:
            Lat_Lon = csv.reader(Lat_Lon_File)  # Read Lat_Lon

            for Coordinates in Lat_Lon:  # Read through each line in Lat_Lon
                if Crime_Line[2] == Coordinates[0]:  # If City in Crime_Report is equal to City in Lat_Lon
                    Crime_Line.pop(0)  # Pop ORI
                    Crime_Line.pop(14)  # Pop Source
                    Crime_Line.pop(14)  # Pop URL
                    Crime_Line.insert(14, Coordinates[3])  # Insert Latitude to Crime Report
                    Crime_Line.insert(15, Coordinates[4])  # Insert Longitude to Crime Report
                    with open('Crime Report.csv', 'a') as Report:  # Open Crime Report as append
                        C_Report = csv.writer(Report)  # Write to C_Report
                        C_Report.writerow(Crime_Line)  # Write to C_Report

                    break

# Read C_Report
C_Report = pd.read_csv('Crime Report.csv')

# Create a 3d visualization
fig = px.scatter_3d(C_Report,
                    x = C_Report['violent_crime'],  # x-axis
                    y = C_Report['population'],  # y-axis
                    z = C_Report['year'],  # x-axis
                    hover_name = 'city_name',  # hover name
                    color = C_Report['population'],  # Point color
                    size = C_Report['population'],  # Point size
                    animation_group = C_Report['year'],  # Animation
                    width = 1200,
                    height = 900,
                    title = 'Crime in Major US Cities'
                )

fig.show()

fig2 = px.scatter_mapbox(C_Report,
                    lat = C_Report['Latitude'],
                    lon = C_Report['Longitude'],
                    hover_name = 'city_name',
                    color = C_Report['population'],
                    size = C_Report['population'],
                    width = 1200,
                    height = 900,
                    title = 'Crime in Major US Cities'
                )

fig2.update_layout(mapbox_style='open-street-map')

fig2.show()

