import pandas as pd

data = pd.read_csv('data.csv')  # Чтение данных из CSV файла
print(data.head())  # Просмотр первых 5 строк
data["value"] = pd.to_numeric(data["value"], errors='coerce') # Перевод значений столбца valueв числа, если нет такой возможности, замена на NaN
mean_values = data["value"].mean()  # Подсчет среднего значения по столбцу
print(mean_values)


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
squared = arr ** 2 + 1  # Математические операции
print(squared)
mean = np.mean(squared)  # Вычисление среднего значения
print(f'Mean: {mean}')

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] # Данные для графика
y = [2, 3, 5, 7, 11] # Данные для графика

plt.plot(x, y, marker='o') # Создание линейного графика
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()