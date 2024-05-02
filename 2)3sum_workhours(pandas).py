import pandas as pd

data = [
    "Андрей 9",
    "Василий 11",
    "Роман 7",
    "X Æ A-12 45",
    "Иван Петров 3",
    "Андрей 6",
    "Роман 11"
]

# Into dataframe
df = pd.DataFrame([x.rsplit(' ', 1) for x in data], columns=['Name', 'Hours'])
df['Hours'] = df['Hours'].astype(int)

# Group and count
result = df.groupby('Name')['Hours'].agg([list, sum]).rename(columns={'list': 'Hours', 'sum': 'Total'})
print(result)
