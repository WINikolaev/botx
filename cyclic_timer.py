import  threading
from    threading import Thread



class СyclicTimer(Thread):
    __count = 0
    """An emergency switch for emergency shutdown the while"""
    _emergency_switch = False
    def __init__(self, period, name=None, args=None, kwargs=None):
        if not name:
            name = "СyclicTimerThread{0}".format(self.__class__.count + 1)
            self.__class__.__count += 1

        Thread.__init__(self, name=name)
        self.period = period
        self.name   = name
        self.args   = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}

        self._event         = threading.Event()
        self.handlerLock    = threading.Lock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stop_thread()

    def _reinitialize_thread(self):
        if self.is_alive():
            return 1
        self._event.clear()
        Thread.__init__(self, name=self.name)

    def _stop_thread(self):
        """Stop the timer if it hasn't finished yet."""
        self._event.set()

    def run(self):
        while not self._event.wait(self.period) and not self._emergency_switch and self.is_alive():
            try:
                with self.handlerLock:
                    self.handler()
            except Exception as E:
                print('EXCEPT: ', E)
                break
        self._event.set()

    def handler(self):
            pass
