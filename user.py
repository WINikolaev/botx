import os
import copy
import pickle
import random
import datetime
import bot_button
import handler_photos

from cyclic_timer import СyclicTimer as timer


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



class HandlerUsers(timer):
    usersDict = {}
    def __init__(self, period, name=None, bot=None, directory_way=None, backup_name=None):
        timer.__init__(self, period, name=name)
        self.bot = bot
        self.__directory_way    = directory_way if directory_way is not None else ''
        self.__backup_name      = backup_name if backup_name is not None else 'backup'
        self.__backup_way       = '{}{}.pickle'.format(self.__directory_way, self.__backup_name)

        self.__load_backup()

    def __load_backup(self):
        if os.path.exists(self.__backup_way):
            with open(self.__backup_way, 'rb') as bp:
                self.usersDict = pickle.load(bp)
        print('usersDict has -> ', self.usersDict)

    def end(self):
        self._stop_thread()

    def handler(self):
        print('usersDict: ', self.usersDict)
        with open(self.__backup_way, 'wb') as bp:
            pickle.dump(self.usersDict, bp)

        if self.bot:
            i = 0
            for key in self.usersDict.keys():
                while i < 1:
                    self.bot.send_message(int(key), 'backup data at {}'.format(datetime.datetime.now()))
                    i += 1