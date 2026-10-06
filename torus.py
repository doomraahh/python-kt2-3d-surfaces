import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (регистрирует projection='3d')

fig = plt.figure(figsize=(7, 6))
fig.suptitle("Тороидальная функция в трёхмерном пространстве", fontsize=14, fontweight="bold")

ax = fig.add_subplot(111, projection="3d")

R, r = 3, 1  # большой и малый радиус тора
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
U, V = np.meshgrid(u, v)
X = (R + r * np.cos(V)) * np.cos(U)
Y = (R + r * np.cos(V)) * np.sin(U)
Z = r * np.sin(V)

ax.plot_surface(X, Y, Z, cmap="plasma", edgecolor="none")
ax.set_title("Тор (R=3, r=1)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.tight_layout()
fig.savefig("torus.png", dpi=150)
print("Сохранено: torus.png")

plt.show()
