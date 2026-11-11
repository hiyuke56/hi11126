import pandas as pd
scores = pd.Series([70, 80, 90, 65])
print(scores)
print(scores[0])
print(scores[2])
scores2 = pd.Series(
    [70, 80, 90],
    index=["Иванов", "Петров", "Сидорова"]
)
print(scores2["Петров"])

data = {
    "Имя": ["Анна", "Иван", "Олег"],
    "Баллы": [85, 72, 91]
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.columns)
print(df.index)
print(df["Баллы"])
print(df[["Имя", "Баллы"]])
df["Группа"] = ["1ИИ-1", "1ИИ-1", "1ИИ-2"]
df["Курс"] = 1
df["Баллы"] = df["Баллы"] + 5
df["Баллы после бонуса"] = df["Баллы"] + 10
print(df)
print(df.loc[0])
print(df.iloc[1])
print(df.loc[0, "Имя"])
print(df.iloc[0:2])
result = df[df["Баллы"] >= 80]
print(result)
result2 = df[df["Группа"] == "1ИИ-1"]
print(result2)
result3 = df[(df["Баллы"] >= 70) & (df["Баллы"] <= 90)]
print(result3)
print(df["Баллы"].sum())
print(df["Баллы"].mean())
print(df["Баллы"].min())
print(df["Баллы"].max())
print(df["Баллы"].count())
print(df.head())
print(df.head(2))
print(df.tail(2))
df.info()
print(df.dtypes)
print(df.describe())