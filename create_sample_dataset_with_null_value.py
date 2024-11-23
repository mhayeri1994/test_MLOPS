import pandas as pd
import numpy as np

data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 30, np.nan, 35, 20, 40, 45, 50, np.nan, 55],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Income': [50000, 60000, 70000, np.nan, 40000, 80000, np.nan, 90000, 100000, 110000],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', np.nan, 'Master', 'PhD', 'Bachelor', 'Master', 'PhD']
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
