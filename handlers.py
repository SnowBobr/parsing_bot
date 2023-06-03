from loader import dp
from aiogram import types
from scrap import scrap_name_price_img


@dp.message_handler(commands="start")
async def pars_command(message: types.Message):
    await message.delete()
    text = """
    
    """
    await message.answer(text=text)

@dp.message_handler(commands="scrap")
async def scrap_comand(message: types.Message):
    await message.delete()
    await scrap_name_price_img(message)