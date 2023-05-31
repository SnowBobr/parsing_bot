from loader import dp
from aiogram import types


@dp.message_handler(commands="start")
async def pars_command(message: types.Message):
    await message.delete()
    text = """
    
    """
    await message.answer(text=text)