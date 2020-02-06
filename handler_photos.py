import os


class Photos:
    photosLight = [fn for fn in os.listdir('photos/light')]
    photosMedium = [fn for fn in os.listdir('photos/medium')]
    photosHard = [fn for fn in os.listdir('photos/hard')]
