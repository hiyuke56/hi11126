title = input("Название проекта: ")
author = input("Автор: ")
group = input("Группа: ")
members = int(input("Количество участников: "))
status = input("Статус проекта: ")

technologies = ["Python", "Git", "AI"]

project = {
    "title": title,
    "author": author,
    "group": group,
    "members": members,
    "status": status,
    "technologies": technologies,
}

print("=" * 40)
print("ПРОФИЛЬ ИИ-ПРОЕКТА")
print("=" * 40)
print("Название:", project["title"])
print("Автор:", project["author"])
print("Участников:", project["members"])
print("Технологии:", project["technologies"])
print("Первая:", project["technologies"][0])
print("Последняя:", project["technologies"][-1])
print("Всего технологий:", len(project["technologies"]))

new_tech = input("Добавить технологию: ")
project["technologies"].append(new_tech)

check = input("Технология для проверки: ")
if check in project["technologies"]:
    print(check, "— есть в списке")
else:
    print(check, "— нет в списке")

project["status"] = input("Новый статус: ")

print("Итоговый словарь:", project)