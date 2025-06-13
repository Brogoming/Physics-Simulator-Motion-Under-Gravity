import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # m/s^2
v0 = 20   # Initial velocity
t = np.linspace(0, 5, 100)
y = v0 * t - 0.5 * g * t**2

plt.plot(t, y)
plt.title("Vertical Motion Under Gravity")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()