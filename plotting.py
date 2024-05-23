import matplotlib.pyplot as plt
import pandas as pd

fieled_computations = pd.read_csv('traverse_data.csv')

def plot_data(readings):
    code = readings
    easting = code['Easting']
    northing = code['Northing']
    plot = plt.scatter(easting, northing)
    return plt.show()
plot_data(fieled_computations)
