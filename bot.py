from aiogram.filters import Command
from aiogram.types import Message
import aiogram
import re
import requests, random, threading, asyncio, sqlite3
from aiogram import types, F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiohttp.web_routedef import route
from datetime import date
from aiogram import Dispatcher
from handlers import router

async def main():
    bot = aiogram.Bot(token='7279498061:AAF_vm1OjASshZ9AkbioG67F39hkWpeteBQ')
    dp = aiogram.Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())