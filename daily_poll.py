import requests
import time
import os

# 1. ВАШИ ДАННЫЕ (замените на свои)
BOT_TOKEN = "8594558961:AAHdxnAbHLIr62YVbxh5692B7GkxsySmd4o"  # Токен, полученный от BotFather [citation:1]
CHAT_ID = "-1003760902540"     # Chat ID, полученный на шаге 2 [citation:10]

# 2. Параметры опроса
POLL_QUESTION = "Какой язык программирования вы предпочитаете?"  # Вопрос
POLL_OPTIONS = ["Python", "JavaScript", "Java", "C++"]           # Варианты ответов

# 3. URL для отправки опроса через Telegram Bot API
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"

# 4. Параметры запроса (данные опроса)
payload = {
    'chat_id': CHAT_ID,
    'question': POLL_QUESTION,
    'options': POLL_OPTIONS,
    'is_anonymous': False,  # False - имена голосующих будут видны
    'allows_multiple_answers': False, # Разрешить выбор нескольких вариантов
}

# 5. Отправка запроса
try:
    response = requests.post(url, data=payload)
    response.raise_for_status()  # Проверить, успешен ли запрос
    print(f"Опрос успешно отправлен в чат {CHAT_ID}")
except Exception as e:
    print(f"Ошибка при отправке опроса: {e}")
    # Здесь можно добавить логирование ошибки в файл [citation:3]