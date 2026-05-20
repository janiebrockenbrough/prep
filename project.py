import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# True position of the tool
true_position = np.array([2, 3])

# Simulated sensor noise
noise = np.random.normal(0, 0.5, size=2)

# Sensor measurement equals true position plus noise
measured_position = true_position + noise

print("True position:", true_position)
print("Measured position:", measured_position)

# Plot the true and measured positions
plt.scatter(true_position[0], true_position[1], label="True Position")
plt.scatter(measured_position[0], measured_position[1], label="Measured Position")

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Simple Navigation Sensor Simulation")
plt.legend()
plt.grid(True)
plt.show()