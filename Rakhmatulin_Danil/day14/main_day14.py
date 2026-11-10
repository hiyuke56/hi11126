import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions
load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")
messages = [
    ChatMessage(role="system", content=SYSTEM_PROMPT)
]
max_pairs = 3  
with open("chat_history.txt", "a", encoding="utf-8") as file:
    file.write("\n=== Новый запуск ===\n")
print("Чат запущен. Доступные команды: выход, очистить, история.")
with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",
    timeout=60,
) as client:
    while True:
        user_input = input("\nВы: ").strip()
        if not user_input:
            print("Пожалуйста, введите текст.")
            continue
        if user_input.lower() == "выход":
            print("Завершение работы чата.")
            break
        elif user_input.lower() == "очистить":
            messages = messages[:1] 
            print("История диалога очищена.")
            with open("chat_history.txt", "a", encoding="utf-8") as file:
                file.write("История текущего диалога очищена.\n")
            continue
        elif user_input.lower() == "история":
            print(f"Сообщений в памяти: {len(messages)}")
            for m in messages:
                print(f"- {m.role}")
            continue
        messages.append(ChatMessage(role="user", content=user_input))
        request = ChatCompletionRequest(
            messages=messages,
            model_options=ChatModelOptions(
                temperature=0.2,
                max_tokens=400,
                repetition_penalty=1.0
            )
        )
        print("GigaChat печатает")
        try:
            response = client.chat.create(request) 
            answer = response.messages[0].content[0].text
            print(f"\nПомощник: {answer}")
            messages.append(ChatMessage(role="assistant", content=answer))

            with open("chat_history.txt", "a", encoding="utf-8") as file:
                file.write(f"Вы: {user_input}\nПомощник: {answer}\n\n")
            if len(messages) > 1 + (max_pairs * 2):
                messages = [messages[0]] + messages[-(max_pairs * 2):]
                print("[Система: старые сообщения удалены из памяти для экономии контекста]")
        except Exception as e:
            print(f"Ошибка при запросе к API: {e}")
            messages.pop() 