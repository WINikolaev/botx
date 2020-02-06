from cyclic_timer import СyclicTimer as ctimer
import pickle
import os

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


# operation of user
class cData_users(ctimer):
    usersDict = {}
    def __init__(self, period, name, bot):
        ctimer.__init__(self, period=period, name=name)
        self.bot = bot
        # get data
        self._get_data()


    def _get_data(self):
        print('_get_data')
        if os.path.exists('backup.pickle'):
            with open('backup.pickle', 'rb') as bp:
                self.usersDict = pickle.load(bp)

    def save_data(self):
        print('save_data')
        with open('backup.pickle', 'wb') as bp:
            pickle.dump(self.usersDict, bp)


    def end(self):
        self.save_data()
        self.stop()

    def handler(self):
        print('usersDict: ', self.usersDict)
        with self.lock:
            if not self.stop_while:
                return 1
            with open('backup.pickle', 'wb') as bp:
                pickle.dump(self.usersDict, bp)