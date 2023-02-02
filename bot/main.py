from aiogram import Dispatcher
from aiogram.utils import executor

from bot import loop, dp, logger_error, logger_info
from bot.handlers import register_handler


async def register_handlers(dispatcher: Dispatcher):
    register_handler(dispatcher)


async def startup(dispatcher: Dispatcher):
    try:
        await register_handlers(dispatcher)
    except Exception as err:
        logger_error.error(err)
    logger_info.info('Start bot')


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    logger_info.info('Stop bot. Storage closed.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, loop=loop, on_shutdown=shutdown, on_startup=startup)
