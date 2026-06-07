import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.compare import router as compare_router
from handlers.analyze import router as analyze_router
from handlers.check import router as check_router


async def main():

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(compare_router)
    dp.include_router(analyze_router)
    dp.include_router(check_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())