import matplotlib.pyplot as plt

X = [0, 1, 2, 3]
Y = [10, 5, 8, 9]

plt.plot(X, Y)
plt.scatter(X, Y)

plt.title("My First Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()