import os
import pickle
import telebot
from bot_main import getUsersDict

TOKEN = '995249108:AAHv_znFEX_m9Z5Ggoo_M8AxhvxEoUuhsVE'
bot = telebot.TeleBot(TOKEN)


def push_Ad():
    if os.path.exists('backUp/backup.pickle'):
        print('get backaup')
        with open('backUp/backup.pickle', 'rb') as bp:
            usersDict = pickle.load(bp)
            print('##############################')
            for key in usersDict.keys():
                i = 0
                while i < 1:
                    bot.send_message(int(key), 'ты пидор !')
                    i += 1


#push_Ad()
dictUser = getUsersDict()
print(dictUser)
