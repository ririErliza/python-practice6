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

# plt.plot(x,y)
# plt.show()


''' Default X-Points '''

ypoints = np.array([3,8,1,10,5,7])

# plt.plot(ypoints)
# plt.show()


'''--------------------   Marker   --------------------------'''

vAxis = np.array([3,8,1,10])

# plt.plot(vAxis, marker='o', ms=20, mec= 'hotpink', mfc='hotpink')
# plt.show()

# ms = markersize
# mec = markeredgecolor
# mfc = markerfacecolor

'''--------------------   Line   --------------------------'''
#single line

ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, linestyle = 'dotted')
# plt.plot(ypoints, ls = ':', color = 'r')
# plt.show()

# linestyle can be written as ls.
# dotted can be written as :.
# dashed can be written as --.

plt.plot(ypoints, ls = ':', color = 'g', linewidth = '10')
plt.show()