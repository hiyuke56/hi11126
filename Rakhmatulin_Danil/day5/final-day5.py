import numpy as np
scores = np.array([78, 55, 91, 60, 45, 82, 67, 73, 88, 52])
print("Исходный массив:", scores)
print("Количество:", scores.size)
print("Тип элементов:", scores.dtype)
print("Средний балл:", np.mean(scores))
print("Минимальный балл:", np.min(scores))
print("Максимальный балл:", np.max(scores))
print("Сумма:", np.sum(scores))
print("Баллы 60 и выше:", scores[scores >= 60])
print("Баллы ниже 60:", scores[scores < 60])
print("Первые три:", scores[:3])
print("Последние три:", scores[-3:])
scores[2] = 95
print("После замены одного балла:", scores)
new_scores = scores + 5
print("После прибавления 5:", new_scores)
print("Новый средний балл:", np.mean(new_scores))