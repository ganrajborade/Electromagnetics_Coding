import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math as math
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

# Iteration (We assume that the iteration is convergence in maxIter = 500)
print("Please wait for a moment")
for iteration in range(0, maxIter):
    for i in range(1, lenX-1):
        for j in range(1, i):
            T[lenX-1-i, lenX-1-j] = 0.25 * (T[lenX-1-i+1][lenX-1-j] + T[lenX-1-i-1][lenX-1-j] + T[lenX-1-i][lenX-1-j+1] + T[lenX-1-i][lenX-1-j-1])

print("Iteration finished")

plt.title("Potential grid in a wedge capacitor")
#plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)
plt.imshow(T, origin='higher', interpolation=None,cmap='seismic')
y = ((2**(0.5)) - 1)*x
plt.plot(x,y,'k')
print(T)


# Set Colorbar
plt.colorbar()
plt.xlabel('Distance along x-axis from extreme left end of lower capacitor plate')
plt.ylabel('Distance along y-axis from extreme left end of upper capacitor plate')
# Show the result in the plot window
plt.show()

