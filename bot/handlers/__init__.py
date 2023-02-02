from aiogram import Dispatcher

from bot.handlers.handler_check_exchange import start, check_exchange


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start,
                                state="*", commands=['start'])
    dp.register_message_handler(check_exchange, state='*')
