import numpy as np
import matplotlib.pyplot as plt

#variables
life_exp = [ 43.828000000000003, 76.423000000000002, 72.301000000000002, 42.731000000000002, 75.319999999999993, 81.234999999999999, 79.828999999999994, 75.635000000000005, 64.061999999999998, 79.441000000000003, 56.728000000000002, 65.554000000000002, 74.852000000000004, 50.728000000000002, 72.390000000000001, 73.004999999999995, 52.295000000000002, 49.579999999999998, 59.722999999999999, 50.43, 80.653000000000006, 44.741000000000007, 50.651000000000003, 78.552999999999997, 72.960999999999999, 72.888999999999996, 65.152000000000001, 46.462000000000003, 55.322000000000003, 78.781999999999996, 48.328000000000003, 75.748000000000005, 78.272999999999996, 76.486000000000004, 78.331999999999994, 54.790999999999997, 72.234999999999999, 74.994, 71.338000000000022, 71.878, 51.578999999999994, 58.039999999999999, 52.947000000000003, 79.313000000000002, 80.656999999999996, 56.734999999999999, 59.448, 79.406000000000006, 60.021999999999998, 79.483000000000004, 70.259, 56.006999999999998, 46.388000000000012, 60.915999999999997, 70.198000000000008, 82.207999999999998, 73.338000000000022, 81.757000000000005, 64.698000000000008, 70.650000000000006, 70.963999999999999, 59.545000000000002, 78.885000000000005, 80.745000000000005, 80.546000000000006, 72.566999999999993, 82.602999999999994, 72.534999999999997, 54.109999999999999, 67.296999999999997, 78.623000000000005, 77.588000000000022, 71.992999999999995, 42.591999999999999, 45.677999999999997, 73.951999999999998, 59.443000000000012, 48.302999999999997, 74.241, 54.466999999999999, 64.164000000000001, 72.801000000000002, 76.194999999999993, 66.802999999999997, 74.543000000000006, 71.164000000000001, 42.082000000000001, 62.069000000000003, 52.906000000000013, 63.784999999999997, 79.762, 80.203999999999994, 72.899000000000001, 56.866999999999997, 46.859000000000002, 80.195999999999998, 75.640000000000001, 65.483000000000004, 75.536999999999978, 71.751999999999995, 71.421000000000006, 71.688000000000002, 75.563000000000002, 78.097999999999999, 78.746000000000024, 76.441999999999993, 72.475999999999999, 46.241999999999997, 65.528000000000006, 72.777000000000001, 63.061999999999998, 74.001999999999995, 42.568000000000012, 79.971999999999994, 74.662999999999997, 77.926000000000002, 48.158999999999999, 49.338999999999999, 80.941000000000003, 72.396000000000001, 58.555999999999997, 39.613, 80.884, 81.701000000000022, 74.143000000000001, 78.400000000000006, 52.517000000000003, 70.616, 58.420000000000002, 69.819000000000003, 73.923000000000002, 71.777000000000001, 51.542000000000002, 79.424999999999997, 78.242000000000004, 76.384, 73.747, 74.248999999999995, 73.421999999999997, 62.698, 42.383999999999993, 43.487000000000002]
life_exp1950 = [28.8, 55.23, 43.08, 30.02, 62.48, 69.12, 66.8, 50.94, 37.48, 68.0, 38.22, 40.41, 53.82, 47.62, 50.92, 59.6, 31.98, 39.03, 39.42, 38.52, 68.75, 35.46, 38.09, 54.74, 44.0, 50.64, 40.72, 39.14, 42.11, 57.21, 40.48, 61.21, 59.42, 66.87, 70.78, 34.81, 45.93, 48.36, 41.89, 45.26, 34.48, 35.93, 34.08, 66.55, 67.41, 37.0, 30.0, 67.5, 43.15, 65.86, 42.02, 33.61, 32.5, 37.58, 41.91, 60.96, 64.03, 72.49, 37.37, 37.47, 44.87, 45.32, 66.91, 65.39, 65.94, 58.53, 63.03, 43.16, 42.27, 50.06, 47.45, 55.56, 55.93, 42.14, 38.48, 42.72, 36.68, 36.26, 48.46, 33.68, 40.54, 50.99, 50.79, 42.24, 59.16, 42.87, 31.29, 36.32, 41.72, 36.16, 72.13, 69.39, 42.31, 37.44, 36.32, 72.67, 37.58, 43.44, 55.19, 62.65, 43.9, 47.75, 61.31, 59.82, 64.28, 52.72, 61.05, 40.0, 46.47, 39.88, 37.28, 58.0, 30.33, 60.4, 64.36, 65.57, 32.98, 45.01, 64.94, 57.59, 38.64, 41.41, 71.86, 69.62, 45.88, 58.5, 41.22, 50.85, 38.6, 59.1, 44.6, 43.58, 39.98, 69.18, 68.44, 66.07, 55.09, 40.41, 43.16, 32.55, 42.04, 48.45]
# Scatter plot


# Histogram of life_exp, 15 bins

plt.hist(life_exp, bins= 15)
# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins= 15)

# Show and clear plot again
plt.show()
plt.clf()

print(life_exp)

