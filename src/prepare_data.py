import pandas as pd
from sklearn.datasets import load_iris
import os

# creating data directory if it doesnt exist
os.makedirs('data', exist_ok=True)

# Loading dummy data (Iris dataset)
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Save as CSV

df.to_csv('data/iris.csv', index=False)
print("Data save to data/iris.csv")