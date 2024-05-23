import csv
import os
import math
import matplotlib.pyplot as plt

def read_traverse_data(file_path):
    data = []
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        return data
    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            if header != ['Point', 'Easting', 'Northing']:
                print("Error: Incorrect CSV format.")
                return data
            data = [(int(row[0]), float(row[1]), float(row[2])) for row in csv_reader if len(row) == 3]
    except Exception as e:
        print(f"Error: {e}")
    return data

def calculate_traverse_characteristics(data):
    if not data:
        return None
    num_points, eastings, northings = len(data), [point[1] for point in data], [point[2] for point in data]
    return num_points, min(eastings), max(eastings), min(northings), max(northings)

def distance_and_bearing(point1, point2):
    dx, dy = point2[1] - point1[1], point2[2] - point1[2]
    dist = math.sqrt(dx*2 + dy*2)
    angle = math.degrees(math.atan2(dx, dy))
    if dy == 0:
        bearing = 90 if dx > 0 else (270 if dx < 0 else None)
    else:
        bearing = angle if dx >= 0 and dy > 0 else (180 - angle if dx >= 0 and dy < 0 else (180 + angle if dx < 0 and dy < 0 else 360 - angle))
    return dist, bearing

def visualize_traverse(data):
    if data:
        points, eastings, northings = [point[0] for point in data], [point[1] for point in data], [point[2] for point in data]
        plt.figure(figsize=(8, 6))
        plt.scatter(eastings, northings, c='b', marker='o')
        for i, point in enumerate(data):
            plt.annotate(point[0], (point[1], point[2]), textcoords="offset points", xytext=(0,5), ha='center')
        plt.title('Traverse Visualization')
        plt.xlabel('Easting')
        plt.ylabel('Northing')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("No data to visualize.")

def main():
    file_path = 'traverse_data.csv'
    traverse_data = read_traverse_data(file_path)
    if traverse_data:
        print("Traverse data successfully read:")
        [print(point) for point in traverse_data]
        num_points, min_e, max_e, min_n, max_n = calculate_traverse_characteristics(traverse_data)
        print(f"\nTotal points: {num_points}\nMin Easting: {min_e}\nMax Easting: {max_e}\nMin Northing: {min_n}\nMax Northing: {max_n}")
        visualize_traverse(traverse_data)
    else:
        print("No valid data found.")

if __name__ == "__main__":
    main()