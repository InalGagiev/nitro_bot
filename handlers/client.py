from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types, Bot
from keyboards import catalog_list, earnings_list

# async def cmd_start(message: types.Message):
#     await message.answer(f"Hello", reply_markup=kb_client)


# def register_handlers_client(dp: Dispatcher):
#     dp.register_message_handler(cmd_start, commands='start')
#     dp.register_message_handler(cmd_start, Text(equals='start'))

async def cmd_start(message: types.Message):
    # отправка изображения
    with open('images/header.jpg', 'rb') as photo:
        await message.answer_photo(photo,
                                   #тут мы ообозначаем что будем пользоваться ранее созданной клавиатурой    
                                   reply_markup=catalog_list,
                                   caption=
                                   '''❕Мы рады приветствовать тебя в нашем магазине нитро - NitroStorm, лучшего места для покупки Нитро ты уже не найдёшь!❕

🔔У нас ты можешь купить Нитро всего от 94 рублей! Быстрая оплата и выдача через QR код!🔔

🌟Чтобы купить Нитро, нажми кнопку "Купить", выбирай какое Нитро тебе больше по душе, затем оплачивай удобным способом, дальше сканируй QR код, а после остаётся лишь ждать!🌟

💰Наш проект предоставляет работу любому желающему! За привлечение клиентов мы даём 2-3%, нет... Мы даём 100% от прибыли! До 600 рублей за человека! Интересно? Тогда нажимай на кнопку "Хочу Заработать!" и узнай больше!💰

⚡️Чтобы связаться с тех.поддержкой, нажмите кнопку "Помощь", вы сможете связаться с нами в любом удобном для вас месте!⚡️--''')
    
async def handle_buy_callback(callback_query: types.CallbackQuery):
    with open('images/prices.jpg', 'rb') as photo:
        await callback_query.message.answer_photo(photo,
                                   caption='''💥 Выбери интересующую тебя подписку и покупай!

💜 При нажатии на кнопку с названием нужного вам Нитро вы получите ссылку на платёжную систему, там вы сможете оплатить Нитро удобным для вас способом. Для оплаты через криптовалюту обращайтесь сюда @Nikita1264

💜После оплаты вам следует подождать некоторое время ответа нашей команды. Мы дадим вам QR, который вам нужно будет отсканировать в вашем дискорд приложении и ожидать выдачи Нитро в течении 5-10 минут!'''
                                   )

async def handle_earnings(callback_query: types.CallbackQuery):
    await callback_query.message.answer(reply_markup=earnings_list, text='''💎 Любой начинающий интернет магазин, да и бизнес нуждается в клиентах, наш NitroStorm не исключение, а значит, нам нужна реклама! И ваша помощь для нас самая важная на свете!⚡️

💎 "А что я получу?" - главный интересующий вопрос. Так вот, если вы привлечете нашему магазину клиента, то получите 100% прибыли! Неа, это не опечатка. Вы получите ВСЮ прибыль с клиента, которого вы привлечете!

💎 Вы получите свои деньги за привлечение сразу после того как привлеченный вами клиент оплатит Нитро! То есть шанс обмана с нашей стороны минимален!

Чтобы узнать подробнее о нашем предложении вы можете прочитать небольшую статью в ВК или на нашем дискорд сервере в чате "📘job│заработок"''')

#тут мы регистрируем наши хэндлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(handle_earnings, Text(equals='earnings'))
    dp.register_callback_query_handler(handle_buy_callback, Text(equals='button_pressed'))
    dp.register_message_handler(cmd_start, commands='start')
