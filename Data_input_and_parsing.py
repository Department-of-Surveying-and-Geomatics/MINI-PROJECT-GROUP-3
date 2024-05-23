import csv
with open('traverse_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        try:
            point_number = row[0]
            easting = float(row[1])
            northing = float(row[2])
            print(f'point number: {point_number}')
            print(f'easting: {easting}')
            print(f'northing: {northing}\n')
        except (ValueError,IndexError) as e:
            print("sorry cant proceed")


