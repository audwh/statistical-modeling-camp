import numpy as np
import matplotlib.pyplot as plt

# Generate sample data (independent variable X and dependent variable y)
X = np.arange(1, 11)
y = np.array([2, 4, 5, 4, 5, 6, 7, 8, 9, 10])

# Perform linear regression using NumPy's polyfit
a, b = np.polyfit(X, y, 1)  # slope (a) and intercept (b)

# Predicted values from the model
predicted = a * X + b

# Plot the data points and the regression line
plt.scatter(X, y, label='Data Points')
plt.plot(X, predicted, color='red', label=f'Fit line: y = {a:.2f}x + {b:.2f}')
plt.title('Simple Linear Regression Example')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# Save the plot
plt.savefig('linear_regression_example.png')
plt.show()
