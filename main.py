'''
Cтатистика канала Ted
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("TED Talks.csv")
plt.title('Среднее кол-во просмотров за каждый год')
df[['month', 'year']]=df['date'].str.split(pat=' ',n=1,expand=True)
df.sort_values(by='year', inplace=True)
group=df.groupby('year').median()
print(group)
plt.plot(df['year'],df['views'])
plt.show()
plt.plot(df['year'],df['likes'])
plt.show()
