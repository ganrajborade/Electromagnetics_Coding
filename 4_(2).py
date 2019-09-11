import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
fig = plt.figure(num=1)
fig.clf()
ax = fig.add_subplot(1, 1, 1, projection='3d')

(x, y) = np.meshgrid(np.linspace(-10, 10, 1000), 
                     np.linspace(-10, 10, 1000))
z =(x**2-y**2)

p = ax.plot_surface(x, y, z, cmap=cm.hot)
ax.set(xlabel='x', ylabel='y', zlabel='z', 
       title='Rectilinear Grid')
fig.colorbar(p)
fig.tight_layout()
plt.title("$z = x^2 - y^2$")
plt.show()