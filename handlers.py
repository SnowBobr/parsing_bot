from loader import dp, bot
from aiogram import types
from save_xls import writer
from scrap import array


@dp.message_handler(commands="start")
async def pars_command(message: types.Message):
    await message.delete()
    text = """
    
    """
    await message.answer(text=text)

@dp.message_handler(commands="scrap")
async def scrap_comand(message: types.Message):
    await message.delete()
    writer(array)
    await message.answer(text="parsing succesfuled ended")
    await bot.send_file(chat_id=message.from_user.id, file="pars.xlsx")
