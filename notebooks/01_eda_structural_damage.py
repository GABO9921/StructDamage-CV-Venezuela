# OpenSeismic-VE: Exploratory Data Analysis (EDA) of Structural Damage
# June 24, 2026 - Venezuela Earthquake

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Open Dataset
print("Loading earthquake damage metadata...")
df = pd.read_csv('../dataset/metadata.csv')

# 2. Basic Data Cleaning
df['construction_year'] = pd.to_numeric(df['construction_year'], errors='coerce')

# 3. Analyze Soft Story (Planta Baja Blanda) vs Damage Typology
print("\n--- Structural Analysis: Soft Story Vulnerability ---")
soft_story_impact = pd.crosstab(df['soft_story'], df['damage_typology'])
print(soft_story_impact)

# 4. Visualization: Construction Year and COVENIN Norm Updates
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='construction_year', hue='covenin_norm', multiple='stack', bins=15)
plt.title('Distribution of Damaged Buildings by Construction Year & COVENIN Norm')
plt.xlabel('Year of Construction')
plt.ylabel('Number of Collapses / Severe Damage')
plt.savefig('covenin_analysis.png')
plt.show()

# ---------------------------------------------------------
# TODO FOR CLAUDE AI INTEGRATION:
# 1. Use Claude's Vision capabilities to cross-reference /dataset/images/ 
#    with the 'damage_typology' labeled by students.
# 2. Build a CNN (Convolutional Neural Network) script to automatically 
#    detect 'Severe_Shear_Cracking' vs 'Total Collapse' based on this dataset.
# 3. Automate the generation of the Sa(T) response spectra graphs 
#    comparing USGS M7.5 data with COVENIN 1756 and ASCE 7-22.
# ---------------------------------------------------------
