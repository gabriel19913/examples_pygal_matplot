from die import Die
from matplotlib import pyplot as plt

die = Die()
results = []
# Rolls a six side dice 1000 times
for i in range(1000):
    results.append(die.roll())
freq = []
# Counts the frequence of appearance of each dice number
for i in range(1, die.num_sides + 1):
    freq.append(results.count(i))

# Open the graph window with the ideal size
plt.figure(figsize=(10, 6))

# plt.scatter(range(1, die.num_sides + 1), freq, linewidth=1)
# Generates a bar graph with the frequency of each number
plt.bar(range(1, die.num_sides + 1), freq)

plt.title("Results of rolling one D6 1000 times", fontsize=16)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

# Shows the histogram in a new window
plt.show()
