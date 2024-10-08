# 1. Импорт библиотек
import os
# Библиотека логгировния
import logging
# Ботом будем отправлять сообщения. К Диспетчеру подключаются обработчики; он делает запросы к серверам телеграмма на наличие обновлений
from aiogram import Bot, Dispatcher
# Нужны будут обновления типа Message. Ловим все обновления этого типа
from aiogram.types import Message
# Для обработки команды Старт нужен класс Command. /start, /help и другие
from aiogram.filters.command import Command

# 2. Инициализация объектов
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
# включить логгирование. Уровень сбора информации (в данном случае второй уровень)
logging.basicConfig(level=logging.INFO)

# 3. Обработка команды start. Если бы мы хотели обрабатывать и другие команды, например help, мы бы написали их через запятую commands=['start', 'help']
# Декоратор - это надстройка над уже существующей функцией. Мы таким образом расширяем её функционал.
# объявляем функцию
# асинхронность нужна для того, чтобы параллельно обрабатывать запросы
# указываем атрибуты, которые присваиваем переменной из Message
@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

# 4. Обработка всех сообщений
@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=text)

# 5. Запуск процесса пуллинга
# Запросим Диспетчер обращаться к серверам ТГ на наличие обновлений
if __name__ == '__main__':
    dp.run_polling(bot)
