import telebot
from telebot import types


bot = telebot.TeleBot('6080375267:AAFVgZylGUKlhEUTkjIMSk1PxW2hPgDkDu4')

@bot.message_handler(commands=['start'])
def start_bot(message):
    chat_id = message.chat.id
    text_start = f'<b>Привет, {message.from_user.first_name} ✌️</b>' \
                 f'\nЯ телеграм-бот компании Too Easy Travel, и служу для поиска подходящих отелей в нужном городе' \
                 f'\n\n<b>Вот список моих команд:</b>' \
                 f'\n- Узнать топ самых дешёвых отелей в городе /lowprice' \
                 f'\n- Узнать топ самых дорогих отелей в городе /highprice' \
                 f'\n- Узнать топ отелей, наиболее подходящих по цене и расположению от центра /bestdeal' \
                 f'\n- Узнать историю поиска отелей /history' \
                 f'\n- Помощь управления ботом /help' \
                 f'\n\n<b>Если Вам лень прописывать команды вручную, у меня есть функционал кнопок!</b>' \
                 f'\n<b>С ними ведь удобнее, правда? 😉</b>'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Самые дешёвые отели')
    btn2 = types.KeyboardButton(text='Самые дорогие отели')
    btn3 = types.KeyboardButton(text='Топ отелей')
    btn4 = types.KeyboardButton(text='История поиска')
    btn5 = types.KeyboardButton(text='Помощь')
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(chat_id, text_start, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)