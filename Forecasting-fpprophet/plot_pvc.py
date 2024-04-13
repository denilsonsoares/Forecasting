import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('PVC-2018-2023.xlsx', header=0)

df['Data'] = pd.to_datetime(df['Data'])
df['year'] = df['Data'].dt.year
df['month'] = df['Data'].dt.month
df['month_day'] = df['Data'].dt.strftime('%m-%d')

df = df.sort_values(by='month_day', ascending=False)


# para escolher vários anos, usar o método isin
df = df[df['year'].isin([2018, 2019, 2022, 2023])]

sns.set_style("whitegrid")
plt.figure(figsize=(14, 8))
sns.lineplot(data=df, x='month', y='PVC BRL/tonne', hue='year', palette='tab10', legend='full')

plt.xlabel('Mês/Dia')
plt.ylabel('Preço')
plt.title('Preço do PVC em função do mês/dia')

plt.show()
#plt.savefig('PVC-2018-2023')