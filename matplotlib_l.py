import matplotlib.pyplot as plt
import numpy as np


'''------------------ -   Plotting   --------------------------'''

''' Plotting x and y points '''
xpoints = np.array([0,6])
ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()


''' Plotting Without Line '''
x = np.array([1,8])
y = np.array([3,10])

# plt.plot(x,y, 'o')
# plt.show()


''' Multiple Points '''
# Draw a line in a diagram from position
#  (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)

x = np.array([1,2,6,8])
y = np.array([3,8,1,10])

plt.plot(x,y)
plt.show()


''' Default X-Points '''

