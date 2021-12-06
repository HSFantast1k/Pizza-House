from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

"""
@dp.message_handler(commands=['start', 'help'])
"""


async def command_start(message: types.Message):
    try:
        user_id = message.from_user.id
        await bot.send_message(chat_id=user_id, text='Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(text='Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_HouseBot')


"""
@dp.message_handler(commands=['Режим_работы'])
"""


async def pizza_open_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Вс-Чт - с 9:00 до 20:00,\nПт-Сб - с 10:00 до 23:00.')


"""
@dp.message_handler(commands=['Расположение'])
"""


async def pizza_place_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='ул. Чорного 27.', reply_markup=ReplyKeyboardRemove())


"""
@dp.message_handler(commands=['Меню'])
"""


async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
