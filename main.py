from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

from handlers import client
from handlers import admin
from handlers import other


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    """
    Внемательно TOKEN НЕ ВВЕДЕН
    """
