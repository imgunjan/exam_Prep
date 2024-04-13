import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.arange(0, 1.2, 0.2)

# Calculate the function values
p = 2 * x**2 + 5

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, p)
plt.xlabel("x")
plt.ylabel("p(x)")
plt.title("Plot of p(x) = 2x^2 + 5")
plt.grid()
plt.show()
