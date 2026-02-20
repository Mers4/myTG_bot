import requests
import os
import sys

# Получаем токен и chat_id из переменных окружения (их вы задали в Secrets)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# Проверяем, что токен и chat_id получены
if not BOT_TOKEN or not CHAT_ID:
    print("ОШИБКА: Не заданы BOT_TOKEN или CHAT_ID в секретах GitHub")
    sys.exit(1)

# Настройки опроса
POLL_QUESTION = "ГАЗ в ЗАЛ?"
POLL_OPTIONS = ["ДА", "НЕТ"]

# URL для отправки опроса
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"

# Параметры опроса
payload = {
    'chat_id': CHAT_ID,
    'question': POLL_QUESTION,
    'options': POLL_OPTIONS,
    'is_anonymous': False,  # Будем видеть, кто как голосует
    'allows_multiple_answers': False,  # Только один вариант
}

try:
    print(f"Отправляем опрос в чат {CHAT_ID}...")
    print(f"Вопрос: {POLL_QUESTION}")
    print(f"Варианты: {POLL_OPTIONS}")

    response = requests.post(url, data=payload, timeout=30)
    response.raise_for_status()

    result = response.json()
    if result.get('ok'):
        print("✅ Опрос успешно отправлен!")
        print(f"ID опроса: {result['result']['poll']['id']}")
    else:
        print(f"❌ Ошибка от Telegram API: {result.get('description')}")

except requests.exceptions.Timeout:
    print("❌ Таймаут при отправке запроса")
except requests.exceptions.RequestException as e:
    print(f"❌ Ошибка при отправке: {e}")
except Exception as e:
    print(f"❌ Неожиданная ошибка: {e}")