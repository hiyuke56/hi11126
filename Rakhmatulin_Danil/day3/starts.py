name = input("Имя участника: ")
age = int(input("Возраст: "))
course = input("Курс: ")
consent = input("Согласие на участие (да/нет): ")
score = int(input("Тестовый балл 0–100: "))

print("=" * 40)
print("ПРОВЕРКА ЗАЯВКИ")
print("=" * 40)

if age < 16:
    result = "Возраст не подходит"
elif consent != "да":
    result = "Нет согласия на участие"
else:
    if score >= 90:
        result = "Высокий результат"
    elif score >= 70:
        result = "Хороший результат"
    elif score >= 50:
        result = "Допустимый результат"
    else:
        result = "Результат недостаточен"

print("Участник:", name)
print("Курс:", course)
print("Балл:", score)
print("Результат:", result)
print("Заявка обработана")