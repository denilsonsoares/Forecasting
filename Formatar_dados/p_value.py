import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Create two example dataframes
df1 = pd.DataFrame(np.random.randint(0, 100, size=(100, 10)))
df2 = pd.DataFrame({
    'X1': np.random.randn(10),
    'X2': np.random.randn(10),
    'X3': np.random.randn(10)
})

# Calculate the correlation matrix
correlation_matrix = df1.corr(method='pearson')

# Get the p-values for each correlation
p_values = pd.DataFrame(index=correlation_matrix.index, columns=correlation_matrix.columns)
for col1 in correlation_matrix.columns:
    for col2 in correlation_matrix.index:
        if col1 != col2:
            _, p_value = pearsonr(df1[col1], df1[col2])
            p_values.loc[col1, col2] = p_value

print("Correlation Matrix:")
print(correlation_matrix)
print("\nP-values:")
print(p_values)


