import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visits = [150, 200, 220, 180, 250, 300, 270]

plt.plot(days, visits, color='blue', marker='o')
plt.title("Daily Website Visits")
plt.xlabel("Days")
plt.ylabel("Visits")
plt.grid(True)
plt.show()
