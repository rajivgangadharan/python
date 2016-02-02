
# Written by Rajiv Gangadharan (02 Feb 2016)
# Purpose: Generate a bar plot from a list of velocities and with their mean

import numpy as np
import matplotlib.pyplot as plt


tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229), 
             (238, 99, 99)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)    
    
    
fig = plt.figure(figsize=(12, 14))
ax = fig.add_subplot(111)
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)

ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()

## the data
N = 9
velocity = [25, 32, 34, 32, 25, 32, 30, 24, 32]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.9                      # the width of the bars

velocity_mean = [np.mean(velocity) for i in range(1, N)]



rects2 = ax.bar(ind + width, velocity, width, color=tableau20[20])

# axes and labels
plt.yticks(range(0, 45, 10), [str(x) for x in range(0, 45, 10)], fontsize=22)    
plt.xticks(fontsize=22)
ax.set_xlim(width, len(ind)+width)
ax.set_ylim(0,45)
ax.set_ylabel('Story Points', fontsize=22)
ax.set_xlabel('Iterations', fontsize=22)
#ax.set_title('Velocity for each Iteration')
xTickMarks = ['Iter- '+str(i) for i in range(1,10)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)

mean_line = ax.plot(range(1, N), velocity_mean, label='Mean', 
                    linestyle='--', linewidth=3, color=tableau20[10])

plt.setp(xtickNames, rotation=45, fontsize=22)
legend = ax.legend(loc='upper right')

plt.show()
