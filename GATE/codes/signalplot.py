import numpy as np
import matplotlib.pyplot as plt

# Define the function
def x(t):
  return 2 * np.cos(180 * np.pi * t) * np.cos(60 * np.pi * t)

# Define the time range
t = np.linspace(0, 1, 1000)  # Adjust range and number of points as needed

# Calculate the function values
y = x(t)

# Plot the function
plt.plot(t, y, label=r"$x(t) = 2\cos(180\pi t)\cos(60\pi t)$")

# Add labels and title
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Plot of input signal')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig('signalplot.png')
