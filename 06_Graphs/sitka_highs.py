import csv

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    read = csv.reader(f)
    header_row = next(read)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

