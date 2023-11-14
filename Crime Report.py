import csv
import pandas as pd

with open('ucr_crime_1975_2015.csv', 'r') as Original:
    reader = csv.reader(Original)
    next(reader)
    count = 0

    for line in reader:
        for item in line:
            if line[3].isdigit():
                pass
            else:
                print(line)

                break