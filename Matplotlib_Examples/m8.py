import matplotlib.pyplot as plt

tests = [1, 2, 3, 4, 5]
scores = [78, 82, 85, 88, 90]

plt.plot(tests, scores, color='teal', marker='o')
plt.title("Math Test Scores Over 5 Tests")
plt.xlabel("Test Number")
plt.ylabel("Score")
plt.grid(True)
plt.show()
