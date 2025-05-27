import math
import matplotlib.pyplot as plt
import numpy.random as r

# Initialize array for simulated probabilities
probs = []
# Loop through student numbers from 1 to 40
for n in range(1, 41):
    duplicates = 0
    # Simulate 1000 classrooms
    for _ in range(1000):
        # Randomly draw birthdays (1 to 365)
        birthdays = r.choice(365, n, replace=True)
        # Check for duplicates
        if len(birthdays) != len(set(birthdays)):
            duplicates += 1
    # Probability of duplicates
    probs.append(duplicates / 1000)

# Plot results
plt.plot(range(1, 41), probs, marker='o')
plt.xlabel('Number of Students')
plt.ylabel('Probability of at Least Two Sharing a Birthday')
plt.title('Birthday Problem Simulation')
plt.grid(True)
plt.show()