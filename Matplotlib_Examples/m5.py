import matplotlib.pyplot as plt

hours = list(range(0, 24))
usage = [1.2, 1.0, 0.9, 0.8, 0.7, 0.9, 1.5, 2.0, 2.8, 3.5, 3.2, 3.0, 
         2.8, 2.5, 2.3, 2.8, 3.0, 3.5, 3.0, 2.5, 2.0, 1.8, 1.5, 1.2]

plt.plot(hours, usage, color='purple', marker='o')
plt.title("Electricity Usage Over 24 Hours")
plt.xlabel("Hour of Day")
plt.ylabel("Electricity Usage (kWh)")
plt.grid(True)
plt.show()
