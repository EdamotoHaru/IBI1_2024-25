# First, create lists to store the population of UK countries and China's provinces.
# Print the lists.
# Draw two pie charts to show the population distribution of UK countries and China's provinces.
# Show the pie charts.
uk_countries=[57.11,3.13,1.91,5.45]
china_provinces=[41.88,45.28,61.27,85.15]
uk_countries_name=["England","Wales","Northern Ireland","Scotland"]
china_provinces_name=["Fujian","Jiangxi","Anhui","Jiangsu"]
import matplotlib.pyplot as plt
import numpy as np  
# Create a pie chart for UK countries
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.pie(uk_countries, labels=uk_countries_name, autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution of UK Countries')
# Create a pie chart for China's provinces
plt.subplot(1, 2, 2)
plt.pie(china_provinces, labels=china_provinces_name, autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution of China\'s Provinces')
# Show the pie charts
plt.tight_layout()
plt.show()