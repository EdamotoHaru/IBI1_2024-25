# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
time_steps = 100  # Number of time steps
grid_size = 100  # Size of the grid

# Initialize the population
S = np.ones((grid_size, grid_size))  # All individuals are initially susceptible
I = np.zeros((grid_size, grid_size))  # No one is initially infected
R = np.zeros((grid_size, grid_size))  # No one is initially recovered

# Introduce an initial infected individual
initial_infected = (grid_size // 2, grid_size // 2)  # Center of the grid
I[initial_infected] = 1
S[initial_infected] = 0

# Simulate the SIR model over time
for t in range(time_steps):
    new_S = S.copy()
    new_I = I.copy()
    new_R = R.copy()
    
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the number of infected neighbors
            infected_neighbors = 
                I[i, j] +
                I[i-1, j] if i > 0 else 0 +
                I[i+1, j] if i < grid_size-1 else 0 +
                I[i, j-1] if j > 0 else 0 +
                I[i, j+1] if j < grid_size-1 else 0
            )
            
            # Update S, I, R based on the SIR model equations
            dS = -beta * S[i, j] * infected_neighbors
            dI = beta * S[i, j] * infected_neighbors - gamma * I[i, j]
            dR = gamma * I[i, j]
            
            new_S[i, j] += dS
            new_I[i, j] += dI
            new_R[i, j] += dR
    
    # Update the arrays for the next time step
    S, I, R = new_S, new_I, new_R

# Plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(I, cmap='viridis', interpolation='nearest')
plt.show()