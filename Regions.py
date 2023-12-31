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
# Regional Poverty Bar Chart
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Read in the CSV file for the dataset
file_name = 'C:\\Users\\Commander\\Documents\\tmhts se bootcamp\\poverty.csv'
df = pd.read_csv(file_name, sep=',', header=0, index_col=False)
# Exclude data for the whole country using .loc
condition = (df['Name'] != 'United States')
df = df[condition]
# Create a Hashmap with the different regions of the USA
regions = {
    'West': ['California', 'Alaska', 'Hawaii', 'Washington', 'Oregon',
             'Nevada', 'Idaho', 'Montana', 'Wyoming', 'Utah', 'Colorado',
             'Arizona', 'New Mexico'],  # 13
    'South': ['Texas', 'Oklahoma', 'Arkansas', 'Louisiana', 'Mississippi',
              'Alabama', 'Tennessee', 'Kentucky', 'West Virginia', 'Virginia',
              'North Carolina', 'South Carolina', 'Georgia', 'Florida'],  # 14
    'Northeast': ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts',
                  'Rhode Island', 'Connecticut', 'New York', 'New Jersey',
                  'Pennsylvania', 'Delaware', 'Maryland'],  # 11
    'Midwest': ['Ohio', 'Indiana', 'Illinois', 'Michigan', 'Wisconsin',
                'Minnesota', 'Iowa', 'Missouri', 'North Dakota', 'South Dakota',
                'Nebraska', 'Kansas']  # 12
}


def get_region(state):
    """
    Summary: Sorts all US states into regions
    :param state: Name of the State
    :return: None
    """
    # If the state's name is within the values of the region hashmap,
    # this function then assigns the appropriate region
    for k, v in regions.items():
        if state in v:
            return k
    return None


# Use get_region function to create a new column listing each states respective region
df['Region'] = df['Name'].apply(get_region)
# Set the data types of the columns in the CSV
df.astype({"Region": 'category'})
# Append a column that scales the values by the thousand for readability
df['Number in Poverty in Thousands'] = df.apply(lambda row: row['Number in Poverty'] / 1000, axis=1)
# Pivot the Dataset to show the scaled values for each region per year
df = df.pivot_table(index='Year',
                    values='Number in Poverty in Thousands',
                    columns='Region')
# Set up the parameters and name for the Bar Chart
title = 'USA Poverty Numbers by Region'
ylabel = 'Number in Poverty in Thousands'
df.plot.bar(title=title,
            ylabel=ylabel,
            grid=True,
            legend=True)
plt.tight_layout()
# Save plot as a PNG file with an appropriate name
now = datetime.now()
datetime = now.strftime("%m.%d.%Y %H.%M.%S")
plt.savefig(fname="RegionComp.png")
plt.show()
