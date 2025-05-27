import numpy.random as rand
import matplotlib.pyplot as plt

# Set parameters
transition_rate = 1.8e-9  # Transition probability per cell per day
num_cells = 1e10          # Total number of cells
cluster_size = 100        # Work with clusters of 100 cells
time_increment = 10       # Time increments of 10 days
stages = range(7)         # Stages 0 to 6
days = 1000               # Mouse lifetime
time_points = int(days / time_increment)

# Initialize cells: all in Stage 0
cells = [num_cells / cluster_size] + [0] * 6  # Clusters in each stage

# Store results for plotting
results = [cells[:]]

# Loop through time points
for _ in range(time_points):
    new_cells = [0] * 7
    for stage in stages[:-1]:  # Up to stage 5
        # Number of cells transitioning to next stage
        transitions = rand.binomial(cells[stage], transition_rate * cluster_size * time_increment)
        new_cells[stage] += cells[stage] - transitions
        new_cells[stage + 1] += transitions
    new_cells[6] += cells[6]  # Stage 6 (cancerous) is absorbing
    cells = new_cells
    results.append(cells[:])

# Plot results
results = list(zip(*results))  # Transpose for plotting
for stage in stages:
    plt.plot(range(0, days + time_increment, time_increment), results[stage], label=f'Stage {stage}')
plt.xlabel('Days')
plt.ylabel('Number of Cell Clusters')
plt.title('Cancer Progression Simulation')
plt.legend()
plt.grid(True)
plt.show()