import pandas as pd

# Load data
data = pd.read_csv('data/raw/data.csv')

# Handle missing values
data.fillna(0, inplace=True)

# Save preprocessed data
## Create the directory if it doesn't exist
import os
if not os.path.exists('data/preprocessed'):
    os.makedirs('data/preprocessed')
data.to_csv('data/preprocessed/data.csv', index=False)
