import numpy as np
from scipy.signal import butter, lfilter

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

# Define filter parameters
cutoff_freq = 100  # Critical frequency in Hz
nyq_freq = 0.5 * fs  # Nyquist frequency

# Design the filter
def butter_lowpass(Wn, nyq, order=2):
  b, a = butter(order, Wn, btype='low')
  return b, a

# Calculate normalized critical frequency
Wn = cutoff_freq / nyq_freq

# Apply the filter
b, a = butter_lowpass(Wn, nyq_freq)
y_filtered = lfilter(b, a, y_sampled)

# Plot the original, sampled, and filtered signals
plt.plot(t_sampled, y_sampled, label=r"$x(t)$ (Sampled)")
plt.plot(t_sampled, y_filtered, 'o', markersize=3, label="Filtered (100Hz)")

# Add labels and title
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Plot of original, sampled, and filtered x(t)')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
	
plt.savefig('filteredplot.png')
