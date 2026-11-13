import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions

from prompts import SYSTEM_PROMPT
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")
CHUNKS_DIR = BASE_DIR / "chunks"
CHUNKS_DIR.mkdir(exist_ok=True)
def load_chunks():
    chunks = []
    if not CHUNKS_DIR.exists():
        logging.warning("Папка chunks не найдена.")
        return chunks
    for file_path in CHUNKS_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        chunks.append({"source": file_path.name, "text": text})
    return chunks
chunks = load_chunks()

def main():
    print("=== ИИ-Помощник по французскому языку ===")
    print("Введите 'выход' для завершения.\n")
    
    messages = [
        ChatMessage(role="system", content=SYSTEM_PROMPT)
    ]
    ca_path = BASE_DIR / "certs" / "russian_trusted_root_ca_pem.crt"
    if not ca_path.exists():
         ca_path = "certs/russian_trusted_root_ca_pem.crt"
    with GigaChat(
        credentials=key,
        scope=scope,
        model="GigaChat-2",
        ca_bundle_file=str(ca_path),
        timeout=60,
        verify_ssl_certs=False
    ) as client:
        while True:
            user_input = input("Вы: ").strip()
            if user_input.lower() == "выход":
                print("Завершение работы.")
                break
            if not user_input:
                print("Введите вопрос.")
                continue

            context = 'Контекст\n'
            for i in range(len(chunks)):
                context += f'Чанк {i}: {chunks[i]}\n'
            enriched_prompt = f"""Контекст из базы знаний:

Вопрос пользователя: {user_input}"""
            messages.append(ChatMessage(role="user", content=enriched_prompt))
            try:
                logging.info("Отправка запроса в GigaChat")
                request = ChatCompletionRequest(
                    messages=messages,
                    model_options=ChatModelOptions(temperature=0.5, max_tokens=500)
                )
                response = client.chat.create(request)
                answer = response.messages[0].content[0].text
                print(f"\nРепетитор: {answer}\n")
                messages.append(ChatMessage(role="assistant", content=answer))
                logging.info("Ответ успешно получен")
            except Exception as error:
                logging.error(f"Ошибка API: {error}")
                print(f"\n!!! ТЕКСТ ОШИБКИ: {error} !!!\n")
if __name__ == "__main__":
    main()