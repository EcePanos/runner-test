import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    # Create a grid of complex numbers
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    c = X + Y * 1j  # Complex plane

    # Initialize the z values and divergence tracking
    z = np.zeros_like(c)
    mandelbrot_set = np.zeros(c.shape, dtype=int)

    # Iterate to compute Mandelbrot set
    for i in range(max_iter):
        mask = np.abs(z) <= 2  # Points not yet diverged
        z[mask] = z[mask] ** 2 + c[mask]  # Mandelbrot iteration
        mandelbrot_set[mask] += 1

    return mandelbrot_set

# Parameters
width, height = 1000, 1000
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 100

# Generate Mandelbrot set
mandelbrot_image = mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Plot the Mandelbrot set
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_image, extent=[x_min, x_max, y_min, y_max], cmap='hot', interpolation='bilinear')
plt.colorbar(label='Iterations to escape')
plt.title('Mandelbrot Set')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.savefig('mandelbrot_set.png')  # Save the plot to a file
