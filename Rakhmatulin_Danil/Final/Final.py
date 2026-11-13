import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions
from sentence_transformers import SentenceTransformer
from prompts import SYSTEM_PROMPT

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# --- ИСПРАВЛЕНИЕ ПУТЕЙ ---
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
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

if chunks:
    chunk_texts = [c["text"] for c in chunks]
    chunk_embeddings = model.encode(chunk_texts)
else:
    chunk_embeddings = []

def get_context(query, top_k=2):
    if not chunks:
        return "База знаний пуста."
        
    query_embedding = model.encode(query)
    scores = model.similarity(query_embedding, chunk_embeddings)[0].tolist()
    
    best_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
    
    context = ""
    for i in best_indices:
        if scores[i] > 0.3:
            context += f"--- Источник: {chunks[i]['source']} ---\n{chunks[i]['text']}\n\n"
            
    return context if context else "Подходящих материалов в базе не найдено."

def main():
    print("=== ИИ-Помощник по французскому языку ===")
    print("Введите 'выход' для завершения.\n")
    
    messages = [
        ChatMessage(role="system", content=SYSTEM_PROMPT)
    ]

    # Указываем правильный путь к сертификату через BASE_DIR
    ca_path = BASE_DIR / "certs" / "russian_trusted_root_ca_pem.crt"
    
    # Если файла нет, попробуем найти его по старому пути на всякий случай
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
            
            context = get_context(user_input)
            
            enriched_prompt = f"""Контекст из базы знаний:
{context}

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