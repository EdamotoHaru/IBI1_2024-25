'''
Pseudocode
1. Import necessary libraries
2. Initialize a 100x100 grid to represent the population, with all cells set to 0 (susceptible).
3. Randomly select a coordinate for the initial outbreak and set that cell to 1 (infected).
4. Set the infection probability (beta) and recovery probability (gamma).
5. Create a list to store snapshots of the population at specific time points.
6. Run a loop for 100 days:
    a. Find all currently infected individuals.
    b. For each infected individual, check its 8 neighbors (Moore neighborhood).
    c. If a neighbor is susceptible (0), randomly decide whether it becomes infected based on beta.
    d. For each infected individual, randomly decide whether it recovers based on gamma.
    e. Record the population state at specified time points.
6. Visualize the results using matplotlib.
'''

import numpy as np         
import matplotlib.pyplot as plt  

# Initialize a 100x100 grid to represent the population
population = np.zeros((100, 100))  # Creating a 100x100 grid initialized to 0 (susceptible)
outbreak = np.random.choice(range(100), 2)  # Randomly select a coordinate for the initial outbreak
population[outbreak[0], outbreak[1]] = 1    # Initial infected individual (1) at the outbreak location

# Set parameters
beta = 0.3   # Infection probability (probability of infecting a susceptible neighbor)
gamma = 0.05 # Recovery probability (probability of recovering from infection)

# Set up for snapshots
time_points = [0, 10, 50, 100]       # 需要记录快照的时间点
snapshots = [(0, population.copy())] # 记录初始状态（使用copy防止引用问题）

# Main simulation loop
for t in range(100):
    # (1) Current infected individuals
    current_infected = np.argwhere(population == 1)  
    
    # (2) Infection process
    infected_neighbors = []  # Newly infected neighbors list
    for individual in current_infected: 
        x, y = individual[0], individual[1] 
        
        # Check 8 neighbors (Moore neighborhood)
        for dx in [-1, 0, 1]:       
            for dy in [-1, 0, 1]:  
                if dx == 0 and dy == 0:
                    continue  # Skip the individual itself
                
                # New neighbor coordinates
                nx, ny = x + dx, y + dy
                
                # Check if within bounds
                if 0 <= nx < 100 and 0 <= ny < 100:
                    # Only consider susceptible neighbors (0)
                    if population[nx, ny] == 0:  
                        # Randomly decide to infect based on beta
                        if np.random.rand() < beta:
                            infected_neighbors.append((nx, ny))  
    # Apply infection to susceptible neighbors
    for (x, y) in infected_neighbors:
        population[x, y] = 1  # Turn susceptible (0) into infected (1)
    
    # (3) Recovery process
    for individual in current_infected:  
        x, y = individual[0], individual[1]
        # Randomly decide to recover based on gamma
        if np.random.rand() < gamma:
            population[x, y] = 2  # Turn infected (1) into recovered (2)
    # Record the population state at specified time points
    if (t + 1) in time_points:
        snapshots.append((t + 1, population.copy()))  
# Visualize the results
plt.figure(figsize=(12, 8)) 
for i, (time, pop) in enumerate(snapshots):
    plt.subplot(2, 2, i + 1)            
    plt.imshow(pop, cmap='viridis',        
               interpolation='nearest')  
    plt.title(f'Time = {time}')          
    plt.axis('off')                       

plt.tight_layout() 
plt.show()         
