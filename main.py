from aiogram import Bot, executor, Dispatcher, types
from settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
bot_dispatcher = Dispatcher(bot=bot)


@bot_dispatcher.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'I am echo bot, send a message')


@bot_dispatcher.message_handler()
async def new_user_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(bot_dispatcher)
