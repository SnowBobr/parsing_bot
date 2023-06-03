from aiogram import executor, types
from loader import dp
from config import bobr
from handlers import dp


async def on_bot_startup(dp: dp):
    
    text = f"""Scraping bot ready to use"""
    await dp.bot.send_message(chat_id=bobr, text=text)

    await dp.bot.set_my_commands([
        types.BotCommand("start", "Start"),
        types.BotCommand("help", "Help")
    ])


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_bot_startup, skip_updates=True)
