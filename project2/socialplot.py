#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a pandas DataFrame
data = pd.read_excel('data.xlsx')

# Group the data by year and range start
grouped_data = data.groupby(['Year', 'Range Start']).sum().reset_index()

# Create a dictionary to map the range start values to their respective labels
range_labels = {
    0.00: '0-0.5',
    0.50: '0.5-1',
    1.00: '1-2',
    2.00: '2-3',
    3.00: '3-4',
    4.00: '4-6',
    6.00: '6-10',
    10.00: '10-24'
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the lines for each range
for i, range_start in enumerate(range_labels.keys()):
    range_label = range_labels[range_start]
    range_data = grouped_data[grouped_data['Range Start'] == range_start]
    ax.plot(range_data['Year'], range_data['Audience %'], label=range_label)

# Set the x-axis labels to the years
ax.set_xticks(data['Year'].unique())
ax.set_xticklabels(data['Year'].unique(), rotation=45)

# Set the y-axis label
ax.set_ylabel('Audience %')

# Set the title
ax.set_title('Audience % by Range')

# Add a legend
ax.legend(title='Range')

# Display the plot
plt.show()
