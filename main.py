import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from paymant import *

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("""Привет, я бот для тестовой оплаты на юкассе!
     Напиши команду /buy для оплаты
     
    """)

@dp.message(Command("buy"))
async def cmd_start(message: types.Message):
    await message.answer("""Твои данные для оплаты:
    номер карты - 5555 5555 5555 4477
    срок действия - 11 / 30
    cvc - 343
    Card authentication - 123""")
    paymant_data = payment(100, "это дескрипшин")
    confirmation_url = paymant_data["confirmation"]["confirmation_url"]

    # await check_payment()
    await message.answer(f"{confirmation_url}")
    payment_id = paymant_data["id"]

    payment_dict = json.loads((Payment.find_one(payment_id)).json())
    while payment_dict['status'] == 'pending':
        payment_dict = json.loads((Payment.find_one(payment_id)).json())
        await asyncio.sleep(3)

    if payment_dict['status'] == 'succeeded':
        # print("SUCCSESS RETURN")
        await message.answer("покупка успешна")
        # return True
    else:
        # print("BAD RETURN")
        await message.answer("что-то пошло не так")
        # return False


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())