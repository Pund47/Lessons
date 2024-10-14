import pandas as pd

# Чтение данных из Excel файла
data = pd.read_excel('data.xlsx')
# Вывод первых нескольких строк датафрейма
print(data.head())

# Создание датафрейма
data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22]
})
# Запись в Exсel файл
data.to_excel('output.xlsx', index='name')

df = pd.DataFrame(data,index=['Alice'])
print(df)




