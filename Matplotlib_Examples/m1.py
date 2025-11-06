import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [25, 27, 26, 28, 30, 31, 29]

plt.plot(days, temperature, marker='o')
plt.title("Daily Temperature for One Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
