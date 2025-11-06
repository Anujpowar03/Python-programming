import matplotlib.pyplot as plt

time = [1,2,3,4,5,6,7,8,9,10]
speed = [0,10,25,40,55,65,70,72,70,68]

plt.plot(time, speed, color='red', marker='o')
plt.title("Car Speed over 10 Seconds")
plt.xlabel("Time (s)")
plt.ylabel("Speed (km/h)")
plt.grid(True)
plt.show()
