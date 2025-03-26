#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N = 10000 #Total population
I = 1 #Initial number of infected individuals
R = 0 #Initial number of recovered individuals
S = N - I - R #Initial number of susceptible individuals
beta = 0.3 #Infection rate
gamma = 0.05 #Recovery rate
#Creat arrays to store the values of S, I, and R
Susceptible = [S]
Infected = [I]
Recovered = [R]
time_steps = 1000
#Implement the SIR model
for i in range(time_steps):
    dS = -beta*S*I/N
    dI = beta*S*I/N - gamma*I
    dR = gamma*I
    S += dS
    I += dI
    R += dR
    Susceptible.append(S)
    Infected.append(I)
    Recovered.append(R)
#Plot the results
plt.plot(Susceptible, label='Susceptible')
plt.plot(Infected, label='Infected')
plt.plot(Recovered, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR Model')
plt.legend()
plt.show()
plt.figure (figsize=(6,4),dpi=150)
plt.savefig ('SIR', format = 'pdf')