from aiogram import Router, types, F

router = Router()

@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Хоть кто-то интересуется... уже лучше, а у тебя?')
    else:
        await message.reply('Не понимаю тебя...')

