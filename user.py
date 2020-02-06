from enum import Enum
import bot_button
import handler_photos
import copy
import random


class Level(Enum):
    LIGHT = 0
    MEDIUM = 1
    HARD = 2


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
