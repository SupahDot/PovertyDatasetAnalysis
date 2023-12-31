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
# Percent vs Number Scatter Plot
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from datetime import datetime

# Read in the CSV file for the dataset
file_name = 'C:\\Users\\Commander\\Documents\\tmhts se bootcamp\\poverty.csv'
df = pd.read_csv(file_name, sep=',', header=0, index_col=False)
# Exclude outlier states and countrywide data from the dataset
condition = ((df['Name'] != 'United States') &
             (df['Name'] != 'California') &
             (df['Name'] != 'Florida') &
             (df['Name'] != 'New York') &
             (df['Name'] != 'Texas'))
df = df[condition]
# Append a column that scales the values by the thousand for readability
df['Number in Poverty in Thousands'] = df.apply(lambda row: row['Number in Poverty'] / 1000, axis=1)
# Set up the axes for the Chart
x = df['Number in Poverty in Thousands']
y = df['Percent in Poverty']
plt.scatter(x=x, y=y)
# Apply a Linear Regression to Scatter Plot
x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
Y_pred = linear_regressor.predict(x)
# Name the plot and what information they are referencing
plt.plot(x, Y_pred, color='red')
plt.ylabel('Percent in Poverty')
plt.xlabel('Number in Poverty in Thousands')
title1 = 'Is the Percent in Poverty Proportional to the # in Poverty?'
plt.title(title1)
plt.grid()
plt.tight_layout()
# Save plot as a PNG file with an appropriate name
now = datetime.now()
datetime = now.strftime("%m.%d.%Y %H.%M.%S")
plt.savefig(fname="PercentvsNumpov.png")
plt.show()
