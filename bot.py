from aiogram.filters import Command
from aiogram.types import Message
import aiogram
import re
import requests, random, threading, asyncio, sqlite3
from handlers import router


async def main():
    bot = aiogram.Bot(token='7279498061:AAF_vm1OjASshZ9AkbioG67F39hkWpeteBQ')
    dp = aiogram.Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())