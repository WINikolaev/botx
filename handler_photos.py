import os
import random


class Photos:
    photosLight = [fn for fn in os.listdir('photos/light')]
    photosMedium = [fn for fn in os.listdir('photos/medium')]
    photosHard = [fn for fn in os.listdir('photos/hard')]

    def getStringPhoto (listPhotos: list):
        indexLvL = random.randint(0, (len(listPhotos) - 1))
        stringPhoto = listPhotos[indexLvL]
        listPhotos.remove(stringPhoto)
        return stringPhoto
