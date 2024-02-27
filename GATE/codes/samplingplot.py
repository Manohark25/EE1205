import numpy as np
import matplotlib.pyplot as plt

# Define the function
def x(t):
  return 2 * np.cos(180 * np.pi * t) * np.cos(60 * np.pi * t)

# Define sampling parameters
fs = 200  # Sampling rate in Hz
dt = 1/fs  # Sampling interval

# Define desired time range (adjust as needed)
start = 0
stop = 1

# Create sampled time points
t_sampled = np.arange(start, stop+dt, dt)

# Calculate sampled function values
y_sampled = x(t_sampled)

# Plot the sampled signal
plt.plot(t_sampled, y_sampled, 'o', markersize=3, label="Sampled (200Hz)")

# Add labels and title
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Plot of sampled x(t)')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)

plt.savefig('samplingplot.png')
