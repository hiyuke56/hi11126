project = input("Название проекта: ")
members = int(input("Количество участников: "))
cost_per_member = float(input("Стоимость ресурса на участника: "))
months = int(input("Количество месяцев: "))
responsible = input("Ответственный студент: ")

month_total = cost_per_member * members
total = month_total * months

print("=" * 40)
print("РАСЧЁТ ПРОЕКТА")
print("=" * 40)
print("Проект:", project)
print("Ответственный:", responsible)
print("Участников:", members)
print("Расход за месяц:", month_total)
print("Общий расход:", total)
print("Длина названия:", len(project))
print("Первый символ:", project[0])
print("Последний символ:", project[-1])