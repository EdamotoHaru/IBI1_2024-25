# dalys.py
# Practical 10: Working with Global Health Data

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory (adjust path as needed)
os.chdir("/Users/edamotoharu/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/IBI1_2024-25/Practical10")  # Change to your directory
print("Current directory:", os.getcwd())  # Verify directory
print("Files in directory:", os.listdir())  # List files

# Import dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Explore dataframe
print("\nFirst 5 rows of dataframe:")
print(dalys_data.head(5))
print("\nDataframe info:")
print(dalys_data.info())
print("\nDataframe description:")
print(dalys_data.describe())

# Task: Show the third column (Year) for the first 10 rows
print("\nYear column for first 10 rows:")
print(dalys_data.iloc[0:10, 2])
# Identify the 10th year for Afghanistan
# Assuming Afghanistan is the first entity, rows 0-9 correspond to years 1990-1999
tenth_year_afghanistan = dalys_data.iloc[9, 2]
print(f"The 10th year for DALYs in Afghanistan is: {tenth_year_afghanistan}")  # Should be 1999

# Task: Use Boolean to show DALYs for all countries in 1990
daly_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print("\nDALYs for all countries in 1990:")
print(daly_1990)

# Task: Compute mean DALYs for UK and France
uk_data = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
france_data = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]
uk_mean = uk_data["DALYs"].mean()
france_mean = france_data["DALYs"].mean()
print(f"\nMean DALYs for UK: {uk_mean:.2f}")
print(f"Mean DALYs for France: {france_mean:.2f}")
# Comment: Compare means
if uk_mean > france_mean:
    print("# Mean DALYs in the UK is greater than in France.")
else:
    print("# Mean DALYs in the UK is smaller than or equal to France.")

# Task: Plot DALYs over time for the UK
plt.figure(figsize=(10, 6))
plt.plot(uk_data["Year"], uk_data["DALYs"], 'b*', label="UK DALYs")
plt.xticks(uk_data["Year"], rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs (Disability-Adjusted Life Years)")
plt.title("DALYs in the United Kingdom Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("uk_dalys_plot.png")  # Save plot
plt.show()

# Task: Answer a custom question (Line 60 starts this section)
# Question: How have DALYs in China changed over time compared to the UK?
china_data = dalys_data.loc[dalys_data["Entity"] == "China", ["DALYs", "Year"]]
plt.figure(figsize=(10, 6))
plt.plot(china_data["Year"], china_data["DALYs"], 'r+', label="China DALYs")
plt.plot(uk_data["Year"], uk_data["DALYs"], 'b*', label="UK DALYs")
plt.xticks(china_data["Year"], rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs (Disability-Adjusted Life Years)")
plt.title("DALYs in China vs. UK Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("china_uk_dalys_plot.png")  # Save plot
plt.show()
# Summary statistics for discussion in question.txt
china_mean = china_data["DALYs"].mean()
print(f"Mean DALYs for China: {china_mean:.2f}")