names = ["Иванов", "Петров", "Сидорова", "Козлов", "Смирнова"]
scores = [78, 55, 91, 60, 45]
passed = 0
failed = 0
with open("group_report.txt", "w", encoding="utf-8") as file:
    for i in range(len(names)):
        if scores[i] >= 60:
            result = "зачёт"
            passed = passed + 1
        else:
            result = "незачёт"
            failed = failed + 1
        file.write(names[i] + " --- " + str(scores[i]) + " --- " + result + "\n")
    file.write("\nЗачёт: " + str(passed) + "\n")
    file.write("Незачёт: " + str(failed) + "\n")
with open("group_report.txt", "r", encoding="utf-8") as file:
    print(file.read())