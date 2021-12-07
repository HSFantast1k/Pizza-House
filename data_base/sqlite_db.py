import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute("""CREATE TABLE IF NOT EXISTS menu(
    img TEXT,
    name TEXT PRIMARY KEY,
    description TEXT,
    price REAL);
    """)
    base.commit()


"""
Запись из базы данных, по команде меню в адменке
"""


async def sql_write(state):
    async with state.proxy() as date:
        cur.execute("INSERT INTO menu VALUES (?,?,?,?)", tuple(date.values()))
        base.commit()


"""
Чтение из базы данных, по команде пользователем меню 
"""


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'Название: {ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')


"""
Чтение из базы данных для удаление контента, по команде админа Удалить 
"""


async def sql_read_2():
    return cur.execute('SELECT * FROM menu').fetchall()


"""
Удаление контента, по нажатию по инлайн кнопки админом удалить 
"""


async def sql_delete_command(date):
    cur.execute('DELETE FROM menu WHERE name == ?', (date,))
    base.commit()
