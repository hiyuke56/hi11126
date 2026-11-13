import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions

load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")
print("=== Настройка кулинарного запроса ===")
ingredients = input("Введите имеющиеся продукты (обязательно): ").strip()
time_limit = input("Введите доступное время (необязательно): ").strip()
desired_result = input("Введите желаемый результат (обязательно): ").strip()
if not ingredients:
    print("Ошибка: Поле 'Имеющиеся продукты' не может быть пустым. Завершение работы.")
    exit()
if not desired_result:
    print("Ошибка: Поле 'Желаемый результат' не может быть пустым. Завершение работы.")
    exit()
if not time_limit:
    time_limit = "не указано"
format_choice = input("Выберите формат ответа (1 - краткий, 2 - пошаговый): ").strip()

if format_choice == "1":
    format_text = "Краткий ответ (только суть, без лишних отступлений)."
elif format_choice == "2":
    format_text = "Подробный пошаговый ответ."
else:
    print("Ошибка: Неверный выбор формата. Введите 1 или 2. Завершение работы.")
    exit()
user_prompt = f"""Пожалуйста, приготовь для меня блюдо.
Доступные продукты: {ingredients}
Доступное время: {time_limit}
Желаемый результат: {desired_result}
Требуемый формат: {format_text}
"""
print("\n--- Сформированный запрос (user_prompt) ---")
print(user_prompt)
print("------------------------------------------\n")
request = ChatCompletionRequest(
    messages=[
        ChatMessage(
            role="system",
            content=SYSTEM_PROMPT
        ),
        ChatMessage(
            role="user",
            content=user_prompt
        )
    ],
    model_options=ChatModelOptions(
        temperature=0.2,
        max_tokens=400,
        repetition_penalty=1.0 
    )
)
print("Отправляем запрос в Gigachat")
with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",
    timeout=60,
) as client:
    response = client.chat.create(request)
    answer = response.messages[0].content[0].text
    print("\n=== Ответ помощника ===")
    print(answer)
with open("last_prompt.txt", "w", encoding="utf-8") as file:
    file.write(user_prompt)
with open("last_answer.txt", "w", encoding="utf-8") as file:
    file.write(answer)
print("\n[Успех] Запрос и ответ сохранены в файлы last_prompt.txt и last_answer.txt.")