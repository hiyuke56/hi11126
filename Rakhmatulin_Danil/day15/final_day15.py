from getpass import getpass
from gigachat import GigaChat

key = getpass("Введите ключ: ")

with GigaChat(credentials=key) as client:
    response = client.chat.create("Объясни, что такое API, в 3 предложениях.")
    print(response.messages[0].content[0].text)