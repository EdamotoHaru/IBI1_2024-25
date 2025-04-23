# Pseudocode:
# 1. Create a dictionary with programming languages as keys and usage percentages as values.
# 2. Print the dictionary.
# 3. Use the matplotlib library to plot a bar chart.
# 4. Define a variable to store the programming language to query.
# 5. Retrieve and print the usage percentage of that language from the dictionary.
import matplotlib.pyplot as plt  # Correct import
import numpy as np  # Correct import
# 1. Create a dictionary with programming languages as keys and usage percentages as values.
language_popularity = {"JavaScript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5}

# 2. Print the dictionary.
print("Programming Language Popularity Dictionary:")
print(language_popularity)

# 3. Use the matplotlib library to plot a bar chart.
languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

plt.figure(figsize=(10, 6))
plt.bar(languages, percentages, color='skyblue')
plt.title('Top 5 Programming Languages by Usage Percentage (February 2024)')
plt.xlabel('Programming Languages')
plt.ylabel('Percentage of Developers (%)')
plt.ylim(0, 70)  # Set y-axis limit for better visualization
plt.show()

# 4. Define a variable to store the programming language to query.
query_language = "Python" 

# 5. Retrieve and print the usage percentage of that language from the dictionary.
if query_language in language_popularity:
    print(f"The percentage of developers using {query_language} is {language_popularity[query_language]}%.")
else:
    print(f"{query_language} is not in the top 5 programming languages list.")