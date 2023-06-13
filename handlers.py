from loader import dp
from aiogram import types
from save_xls import writer
from scrap import array
import os

file_path = "pars.xlsx"

@dp.message_handler(commands="start")
async def pars_command(message: types.Message):
    await message.delete()
    text = """
    
    """
    await message.answer(text=text)

@dp.message_handler(commands=["scrap"])
async def scrap_comand(message: types.Message):
    await message.delete()
    writer(array)
    with open("pars.xlsx", "rb") as document:
        await message.answer_document(document=document, caption="parsing succesfuled completed")

    
    if os.path.exists(file_path):
        os.remove(file_path)