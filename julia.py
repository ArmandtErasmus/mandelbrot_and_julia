import numpy as np
import matplotlib.pyplot as plt

def julia(z: complex, c: complex, max_iter: int) -> int:
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter

c_values = [complex(0.285, 0.01), complex(0.38, 0.24), complex(0, -0.75),
            complex(-0.11, 0.85), complex(-0.1, 0.75), complex(-0.7269, 0.1889)]

xmin, xmax = -1, 1
ymin, ymax = -1.5, 1.5
resolution = 2000

num_plots = len(c_values)
num_cols = 3
num_rows = (num_plots + num_cols - 1) // num_cols

fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))

for ax, c in zip(axes.flatten(), c_values):
    result = np.zeros([resolution, resolution], dtype=int)
    for row, Re in enumerate(np.linspace(xmin, xmax, num=resolution)):
        for col, Im in enumerate(np.linspace(ymin, ymax, num=resolution)):
            z = complex(Re, Im)
            result[row, col] = julia(z, c, 100)

    ax.imshow(result.T, cmap="jet", interpolation='bilinear', extent=[xmin, xmax, ymin, ymax])
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title("Julia Set for c = {}".format(c))

for ax in axes.flatten()[num_plots:]:
    ax.axis('off')

plt.tight_layout()
plt.show()
