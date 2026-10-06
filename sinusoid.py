import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

fig = plt.figure(figsize=(7, 6))
fig.suptitle("Двумерная синусоида в трёхмерном пространстве", fontsize=14, fontweight="bold")

ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-10, 10, 150)
y = np.linspace(-10, 10, 150)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, cmap="coolwarm", edgecolor="none")
ax.set_title("z = sin(√(x²+y²))")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.tight_layout()
fig.savefig("sinusoid.png", dpi=150)
print("Сохранено: sinusoid.png")

plt.show()
