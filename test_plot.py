import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sigma = 50

x,y = np.mgrid[-100:100:1,-100:100:1]

z = 1/(2 * np.pi * (sigma**2)) * np.exp(-(x**2+y**2)/(2 * sigma**2))

fig = plt.figure()
# ax = Axes3D(fig)
ax = Axes3D(fig,auto_add_to_figure=False)

fig.add_axes(ax)



# ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='jet',alpha = 0.8)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"),alpha = 0.8)

# # 取消显示x,y,z坐标轴
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])

plt.show()

