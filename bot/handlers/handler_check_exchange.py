from aiogram import types

from bot.handlers.parser_bestchange import get_the_difference


async def start(message: types.Message):
    await message.answer('Приветствуем в тестовом боте для проверки обменников. Пожалуйста, введите название обменника '
                         'следующим сообщением️!')


async def check_exchange(message: types.Message):
    exchange = message.text
    try:
        requested_name, requested_get, leader_name, leader_get = await get_the_difference(exchange)
        text = f"Текущий лидер - <b>{leader_name}</b> с курсом <b>{leader_get}</b> USDT/1BTC\n" \
               f"Ваш выбор - <b>{requested_name}</b> с курсом <b>{requested_get}</b> USDT/1BTC\n" \
               f"\n" \
               f"Разница курсов - <b>{round(abs(requested_get - leader_get), 4)}</b>"
        await message.answer(text)
    except AttributeError as e:
        text = f"К сожалению мы не смогли найти обменник по вашему запросу <b>{exchange}</b>\n\n" \
               f"Пожалуйста, проверьте правильность написания и повторите снова!"
        await message.answer(text)
