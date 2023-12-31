# Copyright 2023, Sadat Gresham
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the “Software”), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# PovertyDatasetAnalysis
# NY-TX Cluster
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from datetime import datetime

# Read in the CSV file for the dataset
file_name = 'C:\\Users\\Commander\\Documents\\tmhts se bootcamp\\poverty.csv'
df = pd.read_csv(file_name, sep=',', header=0, index_col=False)
# Make the Dataset only show data for NY and TX using .loc
condition = ((df['Name'] == 'New York') | (df['Name'] == 'Texas'))
# Append a column that scales the values by the thousand for readability
df['Number in Poverty in Thousands'] = df.apply(lambda row: row['Number in Poverty'] / 1000, axis=1)
df = df[condition]
# Group the values by name and year
df = df.groupby(['Year', 'Name'], as_index=False)['Number in Poverty in Thousands'].sum()
# Couple the value data for NY and TX
features = np.dstack((df[(df['Name'] == 'New York')]['Number in Poverty in Thousands'],
                      df[(df['Name'] == 'Texas')]['Number in Poverty in Thousands']))
# Determine how many clusters to display
# The data was most readable with 3 clusters
kmeans = KMeans(init="random",
                n_clusters=3,
                n_init=10,
                max_iter=300,
                random_state=42)
# Apply the data to your cluster specifications
kmeans.fit(features[0])
# Determine how the datapoints are colored
klabels = kmeans.labels_
colors = mcolors.ListedColormap(
    plt.get_cmap('tab20')(np.linspace(0, 1, np.max(klabels) + 1))
)
label_colors = colors(klabels)
center = colors(np.arange(np.max(klabels) + 1))
# Set up the parameters for the Scatter Plots
plt.subplots(figsize=(8, 6))
x = df[(df['Name'] == 'New York')]['Number in Poverty in Thousands']
y = df[(df['Name'] == 'Texas')]['Number in Poverty in Thousands']
plt.scatter(x=x,
            y=y,
            c=label_colors)
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            c=center, marker="*", s=300)
# Apply a Linear Regression to Scatter Plot
x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
Y_pred = linear_regressor.predict(x)
plt.plot(x, Y_pred, color='red')
# Name the plot and what information they are referencing
plt.ylabel('Texas')
plt.xlabel('New York')
title1 = 'Number of People in Poverty in Texas and New York Through 2011 to 2021, in Thousands'
plt.title(title1)
plt.grid()
plt.tight_layout()
# Save plot as a PNG file with an appropriate name
now = datetime.now()
datetime = now.strftime("%m.%d.%Y %H.%M.%S")
plt.savefig(fname=title1+datetime+"NYCluster.png")
plt.show()
