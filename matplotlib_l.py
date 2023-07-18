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

# single line
ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, linestyle = 'dotted')
# plt.plot(ypoints, ls = ':', color = 'r')
# plt.show()

# linestyle can be written as ls.
# dotted can be written as :.
# dashed can be written as --.

# plt.plot(ypoints, ls = ':', color = 'g', linewidth = '10')
# plt.show()


# multiple lines
y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

#--------------

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()


'''--------------------   Labels   --------------------------'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sport Watch Data", loc= 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

# plt.plot(x,y)
# plt.show()


'''--------------------   Grid   --------------------------'''

x = np.array([76, 83, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sport Watch Data", loc= 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

# plt.plot(x,y, color = 'r')

# plt.grid(color='g', ls='--', linewidth = 0.4)
# plt.show()

'''--------------------   Subplot   --------------------------'''

#plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")

#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

# plt.subplot(1, 2, 1)
# #the figure has 1 row, 2 columns, and this plot is the first plot.

# plt.subplot(1, 2, 2)
# #the figure has 1 row, 2 columns, and this plot is the second plot.

