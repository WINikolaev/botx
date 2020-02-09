import telebot

from telebot.types import Message

import bot_button
import threading
import os
import sys

from user import HandlerUsers
from user import User

TOKEN = ''
if not TOKEN:
    print("ERROR: Not found TOKEN")
    sys.exit(96)
bot = telebot.TeleBot(TOKEN)


def igor():
    # for key in employer.usersDict.keys():
    #     i = 0
    #     while i < 1:
    #         bot.send_message(int(key), '''Количество потоков = {} -> {}'''.format(threading.active_count(),
    #                                                                               threading.enumerate()))
    #         i += 1
    listDeleteUsers = []
    for key in employer.usersDict.keys():
        try:
            bot.send_message(int(key), "Проверка рекламы на удалившегося пользователя!")
        except Exception as E:
            listDeleteUsers.append(key)
            print("Обработка эксепшена! {}".format(E))
            continue
    for key in listDeleteUsers:
        employer.usersDict.pop(key)
    t = threading.Timer(15, igor)
    t.setName('TEST_THREAD')
    t.start()



@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    print("Language is: {}".format(message.from_user.language_code))
    print(message.chat.id)

    with employer.handlerLock:
        employer.usersDict[message.chat.id] = User(message.chat.id, message.from_user.first_name,
                                                   message.from_user.last_name, message.from_user.language_code)

    userTest = employer.usersDict.get(message.chat.id)

    print("TEST RUN CHAR ID {} first_name: {} last_name: {} LANGUAGE: {}".format(userTest.chatId, userTest.first_name,
                                                                                 userTest.last_name,
                                                                                 userTest.language_code))
    bot.send_message(message.chat.id,
                     """
Hello, agents
Well, are you ready to play and get even closer to each other?

I have three levels of sinfulness for you 🔥
Let's check how brave you are and if you can reach the end?

Damn, the rules are simple - I am sending assignments - you are completing them.

‼️If you like the game and want to support its development. 
Donate button available. For more information, click on it ‼️
                     """, reply_markup=bot_button.BotButtonRu.markup_user_buttons)

    bot.send_message(message.chat.id, 'Выберите ваш возраст?', reply_markup=bot_button.BotButtonRu.markup_age_init)


@bot.message_handler(func=lambda message: True)
def echo_gigits(message):
    userObj: User = employer.usersDict.get(message.chat.id)
    if message.text == 'Donate🆘':
        bot.send_message(message.chat.id, 'Выберите категорию:',
                         reply_markup=bot_button.BotButtonRu.markup_inline_lvl)
    elif message.text == 'К выбору категории':
        if userObj.fl_user_agreement:
            bot.send_message(message.chat.id, 'Выберите категорию:',
                             reply_markup=bot_button.BotButtonRu.markup_inline_lvl)
        else:
            bot.send_message(message.chat.id, 'некорректно введены данные, пропишите /start')


@bot.callback_query_handler(func=lambda call: True)
def call_back_handler(call):
    userObj: User = employer.usersDict.get(call.message.chat.id)
    if call.data == 'Less18':
        userObj.fl_more18 = True
        bot.send_message(call.message.chat.id, 'Данная игра предназначена для людей старше 18 лет!')
    elif call.data == 'Between_18_25':
        userObj.age = '18-25'
        bot.send_message(call.message.chat.id, 'Примите пользовательское соглашение:',
                         reply_markup=bot_button.BotButtonRu.markup_user_agreement)
    elif call.data == 'Between_26_33':
        userObj.age = '26-33'
        bot.send_message(call.message.chat.id, 'Примите пользовательское соглашение:',
                         reply_markup=bot_button.BotButtonRu.markup_user_agreement)
    elif call.data == 'Between_34_41':
        userObj.age = '34-41'
        bot.send_message(call.message.chat.id, 'Примите пользовательское соглашение:',
                         reply_markup=bot_button.BotButtonRu.markup_user_agreement)
    elif call.data == 'More_41':
        userObj.age = 'More_41'
        bot.send_message(call.message.chat.id, 'Примите пользовательское соглашение:',
                         reply_markup=bot_button.BotButtonRu.markup_user_agreement)
    elif call.data == 'AcceptAgreement':
        userObj.fl_user_agreement = True
        bot.send_message(call.message.chat.id, 'С какого уровня начнем?',
                         reply_markup=bot_button.BotButtonRu.markup_inline_lvl)
    elif call.data == 'DeclineAgreement':
        userObj.fl_user_agreement = False
        bot.send_message(call.message.chat.id, 'Жаль, ждем вас!',
                         reply_markup=bot_button.BotButtonRu.markup_inline_lvl)
    elif call.data == 'Light':
        userObj.currentLvl = 0
        if len(userObj.listPhotos[0]) != 0:
            namePhoto = userObj.getStringPhoto()
            print("Name photo {}".format(namePhoto))
            photo = open('photos/light/{}'.format(namePhoto), 'rb')
            bot.send_photo(call.message.chat.id, photo, reply_markup=bot_button.BotButtonRu.markup_inline_next_light)
        else:
            userObj.restartLvl()
            bot.send_message(call.message.chat.id, text='''
            Поздравляем вы прошли этот уровень🎉🎊🎉
            Вы справились со всеми заданиями данного уровня✅✅✅
            Вы можете перейти на следующий уровень или повторить этот уровень сначала😏⚡️🔥
            ''', reply_markup=bot_button.BotButtonRu.markup_inline_next_light)
    elif call.data == 'Medium':
        userObj.currentLvl = 1
        if len(userObj.listPhotos[1]) != 0:
            namePhoto = userObj.getStringPhoto()
            print("Name photo {}".format(namePhoto))
            photo = open('photos/medium/{}'.format(namePhoto), 'rb')
            bot.send_photo(call.message.chat.id, photo, reply_markup=bot_button.BotButtonRu.markup_inline_next_medium)
        else:
            userObj.restartLvl()
            bot.send_message(call.message.chat.id, text='''
                    Поздравляем вы прошли этот уровень🎉🎊🎉
                    Вы справились со всеми заданиями данного уровня✅✅✅
                    Вы можете перейти на следующий уровень или повторить этот уровень сначала😏⚡️🔥
                    ''', reply_markup=bot_button.BotButtonRu.markup_inline_next_medium)
    elif call.data == 'Hard':
        userObj.currentLvl = 2
        if len(userObj.listPhotos[2]) != 0:
            namePhoto = userObj.getStringPhoto()
            print("Name photo {}".format(namePhoto))
            photo = open('photos/hard/{}'.format(namePhoto), 'rb')
            bot.send_photo(call.message.chat.id, photo, reply_markup=bot_button.BotButtonRu.markup_inline_next_hard)
        else:
            userObj.restartLvl()
            bot.send_message(call.message.chat.id, text='''
                    Поздравляем вы прошли этот уровень🎉🎊🎉
                    Вы справились со всеми заданиями данного уровня✅✅✅
                    Вы можете перейти на следующий уровень или повторить этот уровень сначала😏⚡️🔥
                    ''', reply_markup=bot_button.BotButtonRu.markup_inline_next_hard)
    elif call.data == 'ChooseCategory':
        bot.send_message(call.message.chat.id, text='Выберите категорию:',
                         reply_markup=bot_button.BotButtonRu.markup_inline_lvl)


if __name__ == '__main__':
    usersDict = {}
    employer = HandlerUsers(period=20, usersDict=usersDict, name="EmployerThread", bot=bot)
    employer.start()

    print("Polling starting")
    bot.polling(timeout=60)
    print("Polling fifnishing")
    print("t join comlete")
    employer.end()
