import matplotlib.pyplot as plt

# Sample data: exam scores for a class
scores = [88, 92, 75, 85, 96, 70, 80, 78, 85, 90, 65, 72, 88, 94, 76, 81, 85, 90, 72, 68]

# Create a histogram with 10 bins
plt.hist(scores, bins=10, edgecolor='black')
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Number of Students')

# Save figure to file
plt.savefig('score_histogram.png')
plt.show()
