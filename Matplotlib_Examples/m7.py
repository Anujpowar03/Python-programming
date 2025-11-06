import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = x**3

plt.plot(x, y1, label="y = x²")
plt.plot(x, y2, label="y = x³")
plt.title("Plot of y = x² and y = x³")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
