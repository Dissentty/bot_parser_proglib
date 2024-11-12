import aiogram, os
import asyncio
from dotenv import load_dotenv
from handlers import router


async def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    bot = aiogram.Bot(token=token)
    dp = aiogram.Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())