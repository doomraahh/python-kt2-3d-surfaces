import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (регистрирует projection='3d')

fig = plt.figure(figsize=(7, 6))
fig.suptitle("Параболоид в трёхмерном пространстве", fontsize=14, fontweight="bold")

ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
ax.set_title("z = x² + y²")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.tight_layout()
fig.savefig("paraboloid.png", dpi=150)
print("Сохранено: paraboloid.png")

plt.show()
