import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *


api = "7716483351:AAGc_uguGtYh9DpuW0Tsix3RKgIU20r1GdA"
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

keyboard1 = ReplyKeyboardMarkup(resize_keyboard = True)
button11 = KeyboardButton(text = "Рассчитать")
button21 = KeyboardButton(text = "Информация")
button31 = KeyboardButton(text = "Купить")
button41 = KeyboardButton(text = "Регистрация")
keyboard1.add(button11)
keyboard1.add(button21)
keyboard1.add(button31)
keyboard1.add(button41)

keyboard2 = InlineKeyboardMarkup()
button12 = InlineKeyboardButton(text = "Рассчитать норму калорий", callback_data = "calories")
button22 = InlineKeyboardButton(text = "Формулы расчета", callback_data = "formulas")
keyboard2.add(button12, button22)

keyboard3 = InlineKeyboardMarkup(resize_keyboard = True)
button13 = InlineKeyboardButton(text = "Продукт 1", callback_data = "product_buying")
button23 = InlineKeyboardButton(text = "Продукт 2", callback_data = "product_buying")
button33 = InlineKeyboardButton(text = "Продукт 3", callback_data = "product_buying")
button43 = InlineKeyboardButton(text = "Продукт 4", callback_data = "product_buying")
keyboard3.add(button13, button23, button33, button43)

@dp.message_handler(text = "Купить")
async def get_buying_list(message):
    items = get_all_products()
    for i in range(0, 4):
        with open(f"{i + 1}.jpg", "rb") as img:
            await message.answer(f'Название: {items[i][1]} | Описание: {items[i][2]} | Цена: {items[i][3]}')
            await message.answer_photo(img)
    await message.answer("Выберете продукт для покупки:", reply_markup = keyboard3)

@dp.callback_query_handler(text = "product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = keyboard2)

@dp.callback_query_handler(text = "formulas")
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5.')
    await call.answer()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text = "Регистрация")
async def sign_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text) is False:
        await state.update_data(username = message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email = message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state = RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await state.finish()
    await message.answer("Регистрация прошла успешно")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text = "calories")
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await state.finish()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = keyboard1)

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)