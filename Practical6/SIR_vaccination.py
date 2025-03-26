#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
def simulate_vaccination(vaccination_rates):
    N = 10000  # Total population
    I = 1  # Initial number of infected individuals
    R = 0  # Initial number of recovered individuals
    V = int(N * vaccination_rates)  # Initial number of vaccinated individuals (with different vaccination rates)
    S = N - I - R - V  # Initial number of susceptible individuals
    beta = 0.3  # Infection rate
    gamma = 0.05  # Recovery rate
    # Create arrays to store the values of I
    Infected = [I]
    time_steps = 1000
    # Implement the SIR model
    for i in range(time_steps):
        infect_rate = beta * I / N
        new_infections = np.random.binomial(S, infect_rate)
        new_recoveries = np.random.binomial(I, gamma)
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries
        #Keep the values of S, I, and R non-negative
        S = max(S, 0)
        I = max(I, 0)
        R = max(R, 0)

        Infected.append(I)

    return Infected

vaccination_rates = np.arange(0, 0.9, 0.1)  # Vaccination rate
# Plot the results
for rate in vaccination_rates:
    Infected = simulate_vaccination(rate)
    plt.plot(Infected, label='Vaccination rate: ' + str(rate*100) + '%')

plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.show()    
plt.figure (figsize=(6,4),dpi=150)
#The code snippet above simulates the SIR model with different vaccination rates. The vaccination rates range from 0% to 80% with a step size of 10%. The results are plotted to show the number of infected individuals over time for each vaccination rate. The plot shows that higher vaccination rates lead to lower infection rates and faster recovery times  