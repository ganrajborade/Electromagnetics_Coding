import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math as math
from pylab import *
# Set maximum iteration
maxIter = 1000

# Set Dimension and delta
lenX = lenY = 50 #we set it rectangular
delta = 1

# Boundary condition

Tbottom = 0

Ttilted = 1
# Initial guess of interior grid
Tguess = 0

# Set colour interpolation and colour map
colorinterpolation = 100
colourMap = plt.cm.jet
x = np.linspace(0,lenX-0.5,100)
# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Set array size and set the interior value with Tguess
T = np.empty((lenX, lenY))
T.fill(Tguess)

# Set Boundary condition

T[:1, :] = Tbottom

for v in range(0,lenY):
	T[v,(lenX-1):] = (4/np.pi)*(math.atan(v/(lenX)))

print("The above formulations for the boundary condition on the right boundary of the meshgrid is done because if we take any boundary fixed value at right boundary,then the plot which will be obtained will satisfy the theoretical calculation only upto a particular point in the meshgrid.After that point the plot becomes slightly distorted because we actually don't know the right boundary condition.So to avoid this disruption we are formulating the value at each point on right boundary according to the theoretical calculation.")

print("*************************************************************************************************")

T[:(lenX-1), :(lenY-1)] = 0
for t in range(lenX):
	T[lenX-1-t,lenX-1-t] = 1

# Iteration (We assume that the iteration is convergence in maxIter = 1000)

for iteration in range(0, maxIter):
    for i in range(1, lenX-1):
        for j in range(1, i):
            T[lenX-1-i, lenX-1-j] = 0.25 * (T[lenX-1-i+1][lenX-1-j] + T[lenX-1-i-1][lenX-1-j] + T[lenX-1-i][lenX-1-j+1] + T[lenX-1-i][lenX-1-j-1])

print("Iteration finished")
itr = np.linspace(0,maxIter-1,maxIter)
plt.title("Potential grid in a wedge capacitor")
#plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)
plt.imshow(T, origin='higher', interpolation=None,cmap='seismic')
y = ((2**(0.5)) - 1)*x
plt.plot(x,y,'k',label= 'potential along the line Φ = 22.5 degrees in the form of a line graph = 0.5V ')
print('Since this line is passing through white boxes sufficiently from start and white box corresponds to 0.5V .Hence the potential along this line is 0.5V ')
print('*********************************************************************************************')
print(T)

print("****************************************")
print("From the graph of Relative error vs Iterations ,we observe that after 600 iteratons,the value of Relative error converges.So minimum 600 iterations in this case are required to get reasonable convergence.")
# Set Colorbar
v = np.linspace(-.1, 2.0, 15, endpoint=True)
plt.colorbar(ticks=v)
plt.xlabel('Distance along x-axis from extreme left end of lower capacitor plate')
plt.ylabel('Distance along y-axis from extreme left end of upper capacitor plate')
# Show the result in the plot window

plt.legend()
plt.show()

