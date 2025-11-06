import matplotlib.pyplot as plt

minutes = list(range(1, 11))
heart_rate = [72, 75, 78, 80, 85, 88, 90, 87, 84, 80]

plt.plot(minutes, heart_rate, color='crimson', marker='o')
plt.title("Heart Rate Over 10 Minutes")
plt.xlabel("Time (minutes)")
plt.ylabel("Heart Rate (BPM)")
plt.grid(True)
plt.show()
