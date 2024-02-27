import numpy as np, matplotlib.pyplot as plt

def mandelbrot(Re: int, Im: int, max_iter: int) -> int:
    c: complex = complex(Re, Im)
    z: complex = 0.0j

    for i in range(max_iter):
        z = z * z + c

        if (z.real * z.real + z.imag * z.imag ) >= 4:
            return i
        
    return max_iter

xmin, xmax = 0.351, 0.3512
ymin, ymax = 0.4330, 0.4331

result = np.zeros([2000, 2000])
for row, Re in enumerate(np.linspace(xmin, xmax, num=2000)):
    for col, Im in enumerate(np.linspace(ymin, ymax, num=2000)):
        result[row, col] = mandelbrot(Re, Im, 100)

plt.figure(dpi=100)
plt.imshow(result.T, cmap = "jet", interpolation='bilinear', extent=[xmin, xmax, ymin, ymax])
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()