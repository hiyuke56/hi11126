import numpy as np
data = np.array([
    [78, 55, 91, 60, 45],
    [82, 67, 73, 88, 52],
    [90, 60, 75, 68, 80]
])
print("Исходная таблица:")
print(data)
print("shape:", data.shape)
print("ndim:", data.ndim)
print("size:", data.size)
print("Общее среднее:", np.mean(data))
print("Среднее по группам:", np.mean(data, axis=1))
print("Среднее по заданиям:", np.mean(data, axis=0))
print("Минимум:", np.min(data))
print("Максимум:", np.max(data))
print("60 и выше:", data[data >= 60])
overall = np.mean(data)
print("Ниже общего среднего:", data[data < overall])
print("Первая строка:", data[0])
print("Последний столбец:", data[:, -1])
print("Фрагмент 2x2:")
print(data[0:2, 1:3])
data[0, 0] = 85
print("После замены одного значения:")
print(data)
new_data = data + 5
print("Новое общее среднее:", np.mean(new_data))