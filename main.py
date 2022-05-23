'''
Cтатистика канала Ted
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("TED Talks.csv")
plt.title('Среднее кол-во просмотров за каждый год')
df.sort_values(by='date', inplace=True)

group=df.groupby('date').median()
print(group)
plt.plot(df['date'],df['views'])
plt.show()