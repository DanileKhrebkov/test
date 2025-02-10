import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Max'],
    'Age': [11, 21, 33],
    'Salary': [25000, 31000, 222222]
}

df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 29]
result = filtered_df[['Name', 'Salary']]

print('Отфильтрованные данные:')
print(result)


