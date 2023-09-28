from telebot.types import Message
from states.user_data import UserInputInfo
from loader import bot

@bot.message_handler(commands=['low'])
def low_function(message: Message):
    bot.set_state(message.from_user.id, UserInputInfo.input_city, message.chat.id)
    bot.send_message(message.from_user.id, 'Поиск дешёвых отелей, введите город: ')

@bot.message_handler(states=UserInputInfo.input_city)
def find_city(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['input_city'] = message.text

    bot.send_message(message.from_user.id, f"Выполняю поиск в городе: {data['input_city']}")