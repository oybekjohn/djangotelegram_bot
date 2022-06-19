from aiogram import Dispatcher
from aiogram.types import Message


def register_handlers(dp: Dispatcher):
    # Register your handlers here
    dp.register_message_handler(simple_handler, commands=["market"])


# Create your handlers here
async def simple_handler(message: Message):
    await message.answer('Hello from "Market" app!')
