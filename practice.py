import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('deliveries.csv')
data['fielder']=data['fielder'].replace(np.nan,"no fielder")
cum=data.loc[data['player_dismissed'].str.contains('kohli',case=False,na=False)]
print(cum)

v=cum['bowler'].value_counts()
# print(v)
b=v.head(10)
print(b)
plt.bar(b.index,b.values,color='blue',width=0.5,label='virat dismissals by bowlers ')
plt.xlabel(
    "Bowlers Names",
    labelpad=10,
    fontsize=12,          # bigger font
    fontweight='bold',    # bold text
    fontstyle='italic',   # italic style
    color='navy'          # dark blue color
)

plt.ylabel(
    "Number of Dismissals",
    labelpad=10,
    fontsize=12,
    fontweight='bold',
    fontstyle='italic',
    color='navy'
)

plt.legend(
    title="Legend Title",         # title above legend items
    title_fontsize=12,            # font size for legend title
    fontsize=10,                  # font size for labels
    loc='upper right',            # position ('upper left', 'lower right', etc.)
    frameon=True,                 # draw a border around legend
    shadow=True,                   # add shadow for effect
    facecolor='whitesmoke',       # background color
    edgecolor='black',            # border color
    fancybox=True,                # rounded corners
    borderpad=1,                  # padding inside the legend box
    labelspacing=0.5               # vertical space between items
)

plt.title(
    "Top 10 bowlers to dismiss Virat Kohli",
    fontsize=16,
    fontweight='bold',
    fontstyle='italic',  # italic style
    color='darkred',
    pad=20,
    loc='center'
)
plt.xticks(
    rotation=45,        # rotate labels so they don't overlap
    fontsize=10,        # font size
    fontweight='bold',  # bold
    fontstyle='italic', # italic style
    color='darkgreen'   # text color
)


plt.ylim(0,11)
plt.yticks(range(0,11,1), rotation=45,        # rotate labels so they don't overlap
    fontsize=10,        # font size
    fontweight='bold',  # bold
    fontstyle='italic', # italic style
    color='darkgreen' )
plt.show()