import numpy as np
from matplotlib import pyplot as plt

weeks = np.arange(1,13,1)
#Weeks ->             W1,W2,W3,W4,W5,W6,W7,W8,W9,W10,W11, W12
features_req =       [1, 1, 4, 3, 1, 1, 0, 0, 0, 0,  0,   0]
features_dev =       [0, 1, 2, 2, 3, 2, 2, 1, 1, 0,  0,   0]
features_tst =       [0, 0, 0, 1, 1, 2, 2, 2, 1, 2,  0,   0]
features_vfy =       [0, 0, 0, 0, 1, 1, 2, 2, 3, 1,  2,   0]
features_dne =       [0, 0, 0, 0, 0, 0, 0, 1, 1, 3,  4,   6]
features = np.row_stack((features_dne, features_vfy, features_tst, 
                         features_dev, features_req))

fig, ax = plt.subplots()
ax.stackplot(weeks, features)

# Add relevant y and x labels and text to the plot
plt.title('Cumulative Flow Diagram')
ax.set_ylabel('Features')
ax.set_xlabel('Weeks')
ax.set_xlim(1, 12)
ax.set_ylim(0, 6)

plt.show()
