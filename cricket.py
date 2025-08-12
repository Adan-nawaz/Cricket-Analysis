import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('deliveries.csv')
d=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
cum=data.loc[data['match_id']==1]
v=cum[0:120]
m=cum[120:239]
c=v.groupby('over')['total_runs'].sum()
b=m.groupby('over')['total_runs'].sum()
n=v.groupby('over')['player_dismissed'].count()
x=m.groupby('over')['player_dismissed'].count()
print(n)






width=0.35
print(c.index)
plt.figure(figsize=(12,6))
plt.title(
    " SRH vs RCB — Epic Clash ",
    fontsize=20,              # Bigger text
    fontweight='bold',        # Bold font
    color='darkorange',       # Title color
    pad=15,                   # Space above plot
    fontname='Comic Sans MS'  # Fun font
)

plt.plot(c.index, c.values, color='lightgreen', linestyle="-", linewidth=2.5, label='SRH inning')
plt.plot(b.index, b.values, color='lightblue', linestyle="-", linewidth=2.5, label='RCB inning')

# SRH wickets
first_label_added = False
q = 1
l = 0
for value in n.values:
    j = 0
    for i in range(value):
        if not first_label_added:
            plt.plot(q + j, c.values[l], 'o', color='red', markersize=8, label='Wicket fallen')
            first_label_added = True
        else:
            plt.plot(q + j, c.values[l], 'o', color='red', markersize=8)
        j += 0.2
    q += 1
    l += 1

# RCB wickets
w = 1
k = 0
for value in x.values:
    j = 0
    for i in range(value):
        plt.plot(w + j, b.values[k], 'o', color='red', markersize=8)  # no label here
        j += 0.2
    w += 1
    k += 1

plt.legend()
plt.xlabel("Over", fontsize=14, fontweight='bold', color='darkgreen', labelpad=12, fontname='Arial')
plt.ylabel("Runs", fontsize=14, fontweight='bold', color='darkblue', labelpad=12, fontname='Arial')

plt.xticks(d, fontsize=12, rotation=45, color='purple', fontweight='bold', fontname='Calibri')

plt.tick_params(axis='x', pad=15) 
plt.yticks(
    [0, 5, 10, 15, 20, 25, 30, 35],
    fontsize=12,
    color='darkred',
    fontweight='bold',
    fontname='Verdana'
)
plt.savefig(
    "sales_chart.png",  # file name + extension
    dpi=300,            # resolution (dots per inch)
    bbox_inches='tight',# trims extra white space
    facecolor='#fcfbf7',  # background color
    transparent=False  # if True, background will be transparent
)
plt.tight_layout()
plt.show()
