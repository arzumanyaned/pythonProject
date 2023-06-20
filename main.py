import telegram
from telegram.error import TelegramError
import time
import asyncio

# Токен вашего бота
TOKEN = "6222707449:AAEtENIPy7GtdeXjdOvA1olxI0kVqtkbQ8Q"
# ID вашего канала
CHAT_ID = "@forwine20" #"@your_channel_id"

# Соединение с ботом
bot = telegram.Bot(token=TOKEN)

# Генерация текста
def generate_text():
    return "Пример текста для вашего каналаОтправка сообщения в ваш канал"
async def send_message(text):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text)
    except TelegramError as e:
        print(e)

# Основной цикл
async def main():
    while True:
        # Генерация текста и отправка сообщения в канал
        await send_message(generate_text())
        # Пауза на 24 часа
        time.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
