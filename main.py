import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
num_countries = 10
num_years = 5
countries = [f'Country {i+1}' for i in range(num_countries)]
years = range(2019, 2019 + num_years)
data = {
    'Country': [],
    'Year': [],
    'GDP_Growth': [],
    'Trade_Balance': []
}
for country in countries:
    for year in years:
        data['Country'].append(country)
        data['Year'].append(year)
        data['GDP_Growth'].append(np.random.normal(loc=2, scale=1)) #Simulate GDP growth with mean 2% and std 1%
        data['Trade_Balance'].append(np.random.normal(loc=0, scale=50)) #Simulate trade balance with mean 0 and std 50
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Analysis ---
# (In a real-world scenario, this section would involve more extensive data cleaning and pre-processing)
# Here, we simply ensure data types are correct.
df['Year'] = df['Year'].astype(int)
df['GDP_Growth'] = df['GDP_Growth'].round(2)
df['Trade_Balance'] = df['Trade_Balance'].round(2)
# --- 3. Visualization ---
# Create a scatter plot to visualize the correlation between GDP growth and trade balance.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='GDP_Growth', y='Trade_Balance', hue='Country', data=df)
plt.title('GDP Growth vs. Trade Balance')
plt.xlabel('GDP Growth (%)')
plt.ylabel('Trade Balance')
plt.grid(True)
plt.tight_layout()
output_filename = 'gdp_vs_trade.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# Create a line plot to show GDP growth over time for each country.
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='GDP_Growth', hue='Country', data=df)
plt.title('GDP Growth Over Time')
plt.xlabel('Year')
plt.ylabel('GDP Growth (%)')
plt.grid(True)
plt.tight_layout()
output_filename = 'gdp_growth_over_time.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Further analysis could include correlation calculations, regression analysis etc.  This is a basic example.