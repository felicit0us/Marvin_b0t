from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import keyboard
from utils.random_fox import fox

router = Router()

@router.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}, чтобы получить информацию обо мне отправьте сообщение "инфо".')


@router.message(Command(commands=['стоп']))
@router.message(Command(commands=['stop']))
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Всего доброго, {message.chat.first_name}!', reply_markup=types.ReplyKeyboardRemove())


@router.message(Command(commands=['инфо', 'info']))
@router.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, я депрессивный бот Marvin, приветствую тебя. У меня мало фукнций, ниже представлена клавиатура с ними:', reply_markup=keyboard)
    

@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису')
    await message.answer_photo(img_fox)
    # img_fox = fox()
    # await bot.send_photo(message.from_user.id, img_fox)


@router.message(Command(commands=['случайное_число', 'random_number']))
@router.message(F.text.lower() == 'случайное число')
async def random_number(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Тебе выпало число: {number}!')

