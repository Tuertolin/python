import matplotlib.pyplot as plt
input_values = [1,2,3,4,5,6]
squares = [1, 4, 9, 16, 25, 20]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart tittle and label axes.
ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick table
ax.tick_params(axis='both', labelsize=14)

plt.show()