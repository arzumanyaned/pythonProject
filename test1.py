import telegram
from telegram.error import TelegramError

import telebot
from web3 import Web3

# Введите токен вашего бота
TOKEN = '6222707449:AAEtENIPy7GtdeXjdOvA1olxI0kVqtkbQ8Q'

# Создайте экземпляр бота
bot = telegram.Bot(token=TOKEN)

# Создайте экземпляр Web3 и установите провайдер Infura
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your_infura_project_id'))

# Функция для получения информации о сети Ethereum
def get_ethereum_info():
    network_id = w3.net.version
    block_number = w3.eth.block_number
    gas_price = w3.eth.gas_price
    return f"Network ID: {network_id}\nBlock Number: {block_number}\nGas Price: {gas_price}"

# Обработка команды /info
@bot.message_handler(commands=['info'])
def handle_info(message):
    info = get_ethereum_info()
    bot.reply_to(message, info)

# Обработка всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, 'Просто напишите /info, чтобы получить информацию о сети Ethereum.')

# Запуск бота
bot.polling()
