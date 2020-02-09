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

    currentLvl = None
    age = None
    fl_more18 = False
    fl_user_agreement = False
    first_name = None
    last_name = None
    language_code = None

    def __init__(self, chatId, first_name: str, last_name: str, language_code: str):
        self.chatId = chatId
        self.first_name = first_name
        self.last_name = last_name
        self.language_code = language_code
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

    def __init__(self, period, usersDict: dict, name=None, bot=None, directory_way=None, backup_name=None):
        timer.__init__(self, period, name=name)
        self.usersDict = usersDict
        self.bot = bot
        self.__directory_way = directory_way if directory_way is not None else ''
        self.__backup_name = backup_name if backup_name is not None else 'backup'
        self.__backup_way = '{}{}.pickle'.format(self.__directory_way, self.__backup_name)

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
