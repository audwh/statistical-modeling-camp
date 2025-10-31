import numpy as np

# Sample data (same as histogram)
scores = [88, 92, 75, 85, 96, 70, 80, 78, 85, 90, 65, 72, 88, 94, 76, 81, 85, 90, 72, 68]

# Calculate descriptive statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev = np.std(scores)

print(f"Mean score: {mean_score:.2f}")
print(f"Median score: {median_score:.2f}")
print(f"Standard deviation: {std_dev:.2f}")
