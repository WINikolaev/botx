import telebot

from telebot.types import Message
from telebot.types import User

import bot_button
import threading
import os
import sys

from bot_data_users import Backuper
from bot_data_users import User

TOKEN = os.getenv('TOKEN')
TOKEN = '
if not TOKEN:
    print("ERROR: Not found TOKEN")
    sys.exit(96)
bot = telebot.TeleBot(TOKEN)



def igor():
    threading.Timer(300, igor).start()
    for key in employer.usersDict.keys():
        i = 0
        while i < 1:
            bot.send_message(int(key), 'Количество потоков = {}'.format(threading.active_count()))
            i += 1



@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    print("Language is: {}".format(message.from_user.language_code))
    print(message.chat.id)

    with employer.lock:
        employer.usersDict[message.chat.id] = User(message.chat.id, 18, "RU")

    userTest = employer.usersDict.get(message.chat.id)

    print("TEST RUN CHAR ID {} AGE {} LANGUAGE {}".format(userTest.chatId, userTest.age, userTest.listPhotos[0]))
    bot.send_message(message.chat.id,
                     """
Hello, agents
Well, are you ready to play and get even closer to each other?

I have three levels of sinfulness for you 🔥
Let's check how brave you are and if you can reach the end?

Damn, the rules are simple - I am sending assignments - you are completing them.

‼️If you like the game and want to support its development. 
Donate button available. For more information, click on it ‼️
                     """, reply_markup=bot_button.BotButtonRu.markup_donate)

    bot.send_message(message.chat.id, 'С какого уровня начнем?', reply_markup=bot_button.BotButtonRu.btn_chooseCategory)

if __name__ == '__main__':
    employer = Backuper(period=1800, name="employer", bot=bot)
    employer.start()
    igor()
    bot.polling(timeout=60)

    employer.end()
