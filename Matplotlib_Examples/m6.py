import matplotlib.pyplot as plt

days = list(range(1, 11))
price = [150, 152, 149, 155, 160, 158, 162, 165, 170, 175]

plt.plot(days, price, color='orange', marker='o')
plt.title("Stock Price Over 10 Trading Days")
plt.xlabel("Day")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()
