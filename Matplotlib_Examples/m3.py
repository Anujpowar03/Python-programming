import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [20000, 25000, 27000, 30000, 35000, 40000]

plt.plot(months, revenue, color='green', marker='o')
plt.title("Company Revenue Growth (6 Months)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()

