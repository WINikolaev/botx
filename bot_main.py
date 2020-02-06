import telebot
from telebot import types
from telebot.types import Message
from telebot.types import User
#import user
import bot_button
import bot_data_users
import threading
import os
import sys
#import timer

TOKEN = os.getenv('TOKEN')
TOKEN = ''
if not TOKEN:
    print("ERROR: Not found TOKEN")
    sys.exit(96)
#print('TOKEN: ', TOKEN)
bot = telebot.TeleBot(TOKEN)

def igor():
    threading.Timer(60.0, igor).start()
    for key in data_users.usersDict.keys():
        i = 0
        while i < 1:
            bot.send_message(int(key), 'Никита помой пол!')
            i += 1



@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    print("Language is: {}".format(message.from_user.language_code))
    print(message.chat.id)
    #global usersDict

    with data_users.lock:
        data_users.usersDict[message.chat.id] = bot_data_users.User(message.chat.id, 18, "RU")

    userTest = data_users.usersDict.get(message.chat.id)

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
    data_users = bot_data_users.cData_users(360, "Thread Backup", bot=bot)
    data_users.start()
    igor()
    bot.polling(timeout=60)

    data_users.end()
