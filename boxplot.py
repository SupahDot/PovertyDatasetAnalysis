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
# Boxplot
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Read in the CSV file for the dataset
file_name = 'C:\\Users\\Commander\\Documents\\tmhts se bootcamp\\poverty.csv'
df = pd.read_csv(file_name, sep=',', header=0, index_col=False)
# Set the data types of the columns in the CSV
df = df.astype({"Year": 'category',
                "Name": 'category',
                "90% Confidence Interval": 'category',
                "90% Confidence Interval.1": 'category'})
# Make the Dataset only show data for the whole country using .loc
condition = (df['Name'] != 'United States')
df = df.loc[condition]
# Append a column that scales the values by the thousand for readability
df['Number in Poverty in Thousands'] = df.apply(lambda row: row['Number in Poverty'] / 1000, axis=1)
# Pivot the columns to Years and the rows to the newly appended scaled column
df = df.pivot(columns='Year', values='Number in Poverty in Thousands')
# Set up the parameters for the box plots
fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 12))
# Show the outliers in one plot and hide them in the other
df.boxplot(showfliers=False, return_type='axes', ax=ax1)
df.boxplot(ax=ax2)
# Ensure the chart starts at 0
ax1.set_ylim(0)
# Name the plots and what information they are referencing
title1 = "Poverty Estimates Across the USA from 2011 to 2021 (Outliers Excluded)"
ax1.set_title(title1)
ax1.set_xlabel("Year")
ax1.set_ylabel("# of People in Poverty By State in Thousands")
title2 = "Poverty Estimates Across the USA from 2011 to 2021"
ax2.set_title(title2)
ax2.set_xlabel("Year")
ax2.set_ylabel("# of People in Poverty By State in Thousands")
plt.tight_layout()
# Change font size for readability
plt.rc('axes', labelsize=30)
# Save plot as a PNG file with an appropriate name
now = datetime.now()
datetime = now.strftime("%m.%d.%Y %H.%M.%S")
plt.savefig(fname=title2 + datetime + "boxplots.png")
plt.show()
