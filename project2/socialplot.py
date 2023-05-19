#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('data.xlsx')

grouped_data = data.groupby(['Year', 'Range Start']).sum().reset_index()

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

fig, ax = plt.subplots()

for i, range_start in enumerate(range_labels.keys()):
    range_label = range_labels[range_start]
    range_data = grouped_data[grouped_data['Range Start'] == range_start]
    ax.plot(range_data['Year'], range_data['Audience %'], label=range_label)

ax.set_xticks(data['Year'].unique())
ax.set_xticklabels(data['Year'].unique(), rotation=45)

ax.set_ylabel('Audience %')

ax.set_title('Audience % by Range')

ax.legend(title='Range')

plt.show()
