import aiogram
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
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
from single import parsing

bot = aiogram.Bot(token='7279498061:AAF_vm1OjASshZ9AkbioG67F39hkWpeteBQ')
dp = aiogram.Dispatcher()
router = Router()

@router.message(Command('start'))
async def start_handler(msg: Message):
    url_photo = 'https://media.proglib.io/posts/2024/11/06/8cfb6270920350b05e23957fc3a8bc8d.png'
    await bot.send_photo(chat_id=msg.chat.id, photo=url_photo, caption=parsing())
