""" Plot the harmonic mean (F1 score) and arithmetic mean of sample values of precision and recall. """

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


pr = np.arange(.1, 1.1, .2)
re = pr
f1 = np.array([(2 * p * r) / (p + r) for p in pr for r in re]).reshape((len(pr), len(pr)))
print pr
print re
print f1

# plot F1 (harmonic mean of precision and recall)
fig = plt.figure(figsize=plt.figaspect(2.))
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax.set_xlabel('precision')
ax.set_ylabel('recall')
ax.set_zlabel('F1 (harmonic mean)')
X = np.arange(0.1, 1.1, 0.1)
Y = np.arange(0.1, 1.1, 0.1)
X, Y = np.meshgrid(X, Y)
Z = (2. * X * Y) / (X + Y)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)

# plot arithmetic mean of precision and recall
ax = fig.add_subplot(2, 1, 2, projection='3d')
ax.set_xlabel('precision')
ax.set_ylabel('recall')
ax.set_zlabel('arithmetic mean')
Z = (X + Y) / 2.
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
