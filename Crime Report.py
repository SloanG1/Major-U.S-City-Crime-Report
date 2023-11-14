import csv
import plotly.graph_objects as go
import pandas as pd

with open('ucr_crime_1975_2015.csv', 'r') as Crime:
    Crime_Report = csv.reader(Crime)
    Title_Line = ''

    for Line in Crime_Report:
        if Title_Line == '':
            Line.pop(0)
            Line.pop(14)
            Line.pop(14)
            Line.insert(14, "Latitude")
            Line.insert(15, "Longitude")
            Title_Line = Line
            with open('Crime Report.csv', 'w') as Report:
                C_Report = csv.writer(Report)
                C_Report.writerow(Title_Line)

        with open('us-cities-top-1k.csv', 'r') as Lat_Lon:
            reader = csv.reader(Lat_Lon)

            for Pop in reader:

                if Line[2] == Pop[0]:
                    Line.pop(0)
                    Line.pop(14)
                    Line.pop(14)
                    Line.insert(14, Pop[3])
                    Line.insert(15, Pop[4])
                    print(Line)
                    with open('Crime Report.csv', 'a') as Report:
                        C_Report = csv.writer(Report)
                        C_Report.writerow(Line)

                    break