import threading
import telebot

class myThread():
    # init our thread
    def __init__(self,  sec, name=None):
        self.sec = sec
        self.name = name
        self.thread = threading.Timer(self.sec, self.func_thread)
        #self.lock = threading.Lock()
        if self.name:
            self.thread.setName(self.name)

    def reinit(self, sec, name=None):
        # if old thread alive we have to kill it.
        if self.thread.is_alive():
            self.thread.cancel()

        self.sec = sec
        self.name = name
        self.thread = threading.Timer(self.sec, self.func_thread)
        #self.lock = threading.Lock()
        if self.name:
            self.thread.setName(self.name)

    def start_thread(self):
        self.thread.start()

    def stop_thread(self):
        if self.thread.is_alive():
            self.thread.cancel()

    # def lock(self):
    #     print('lock')
    #     self.lock.acquire()

    # def unlock(self):
    #     self.lock.release()

    def func_thread(self):
        # with self.lock:
        #     print("get hand")
        #     self.handler()
        self.handler()
        self.thread = threading.Timer(self.sec, self.func_thread)
        if self.name:
            self.thread.setName(self.name)
        self.thread.start()

    def get_name(self):
        return self.thread.getName()

    def handler(self):
        pass


class adverb(myThread):
    def __init__(self, sec, bot : telebot.TeleBot, usersDict, name=None):
        myThread.__init__(self, sec, name)
        self.bot = bot
        self.usersDict = usersDict

        # here we can get our pickle file

    def handler(self):
        print("backup handler: ", self.get_name())
        # here we can resave our backup file
        for key in self.usersDict.keys():
            i = 0
            photo = open('photos/1xbet.jpg', 'rb')
            btn_ad = telebot.types.InlineKeyboardMarkup()
            btn_ad.add(telebot.types.InlineKeyboardButton('Перейти', "https://vk.com/w.igornikolaev"))
            while i < 1:
                #self.bot.send_message(int(key), 'ты пидор !')
                self.bot.send_photo(int(key), photo, '''https://core.telegram.org/bots Use this method to send audio files, 
                if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. 
                On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, 
                this limit may be changed in the future.
                ''',
                reply_markup = btn_ad
                )
                i += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_thread()