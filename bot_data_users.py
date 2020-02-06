from cyclic_timer import СyclicTimer
import pickle
import os
import datetime

from enum import Enum
import bot_button
import handler_photos
import copy
import random


# struct for a user
class User:
    language_ru = False
    language_en = False
    currentLvl = None

    def __init__(self, chatId, age=None, language=None):
        self.chatId = chatId
        self.age = age
        if language == 'RU':
            self.button = bot_button.BotButtonRu
        elif language == 'EN':
            self.button = bot_button.BotButtonEn
        self.listPhotos = [copy.deepcopy(handler_photos.Photos.photosLight),
                           copy.deepcopy(handler_photos.Photos.photosMedium),
                           copy.deepcopy(handler_photos.Photos.photosHard)]

    def restartLvl(self):
        currentLvl = self.currentLvl
        if currentLvl == 0:
            self.listPhotos[currentLvl] = copy.deepcopy(handler_photos.Photos.photosLight)
        elif currentLvl == 1:
            self.listPhotos[currentLvl] = copy.deepcopy(handler_photos.Photos.photosMedium)
        elif currentLvl == 2:
            self.listPhotos[currentLvl] = copy.deepcopy(handler_photos.Photos.photosHard)

    def getStringPhoto(self):
        currentLvlPhotos = self.listPhotos[self.currentLvl]
        indexPhoto = random.randint(0, (len(currentLvlPhotos) - 1))
        stringPhoto = currentLvlPhotos[indexPhoto]
        currentLvlPhotos.remove(stringPhoto)
        return stringPhoto

    def setCurrentLvl(self, currentLvl: int):
        self.currentLvl = currentLvl



''' Class for operate on users like backup data'''
class Backuper(СyclicTimer):
    usersDict = {}
    def __init__(self, period, name, bot=None):
        СyclicTimer.__init__(self, period=period, name=name)
        self.bot = bot
        self.__get_data()

    ''' if we found backup.pickle file we can think that we have backup data.
        So, we need to get it.
    '''
    def __get_data(self):
        if os.path.exists('backup.pickle'):
            with open('backup.pickle', 'rb') as bp:
                self.usersDict = pickle.load(bp)
        print('usersDict has -> ', self.usersDict)

    def save_data(self):
        with open('backup.pickle', 'wb') as bp:
            pickle.dump(self.usersDict, bp)
        print('Data saved')

    def end(self):
        self.save_data()
        self._stop()

    def handler(self):
        print('usersDict: ', self.usersDict)
        if self.stop_while:
            return 1

        with self.lock:
            print('backup data')
            with open('backup.pickle', 'wb') as bp:
                pickle.dump(self.usersDict, bp)

        if self.bot:
            for key in self.usersDict.keys():
                i = 0
                while i < 1:
                    self.bot.send_message(int(key), 'backup data at {}'.format(datetime.datetime.now()))
                    i += 1