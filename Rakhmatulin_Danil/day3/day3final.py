languages = ["Python", "Java", "C++"]
print(languages)
print(languages[0])
print(languages[-1])
print(len(languages))
languages[1] = "JavaScript"
languages.append("Go")
languages.insert(1, "Java")
languages.remove("Go")
languages.pop()
print(languages)
print("Python" in languages)
print("Go" in languages)
student = {"name": "Анна", "age": 18, "group": "1ИИ-1-11"}
print(student["name"])
student["age"] = 19
student["city"] = "Москва"
student.pop("city")
print(student)
print(len(student))
print("name" in student)