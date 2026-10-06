import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (регистрирует projection='3d')

fig = plt.figure(figsize=(7, 6))
fig.suptitle("Анимация: бегущая волна двумерной синусоиды", fontsize=13, fontweight="bold")

ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_zlim(-1.2, 1.2)


def update(frame):
    ax.clear()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_zlim(-1.2, 1.2)
    ax.set_title(f"z = sin(√(x²+y²) - {frame * 0.3:.1f})")

    phase = frame * 0.3
    Z = np.sin(R - phase)
    surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", edgecolor="none")
    return (surf,)


n_frames = 40
anim = FuncAnimation(fig, update, frames=n_frames, interval=80, blit=False)

writer = PillowWriter(fps=15)
anim.save("wave_animation.gif", writer=writer)
print("Сохранено: wave_animation.gif")

plt.show()
