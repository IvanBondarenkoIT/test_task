from aiogram import Bot, Dispatcher, F
from core.handlers.basic import get_start, get_text

import asyncio
import logging
from core.settings import settings


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Hello. Bot is starts")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Hello. Bot is closed")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, F.text == "/start")
    dp.message.register(get_text, F.text)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
