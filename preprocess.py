import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv('data/raw/data.csv')

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Encode categorical variables
data['category'] = pd.Categorical(data['category']).codes

# Scale data
scaler = StandardScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])

# Save preprocessed data
data.to_csv('data/preprocessed/data.csv', index=False)

