import threading
from threading import Thread



class СyclicTimer(Thread):
    stop_while = False
    def __init__(self, period, name=None, args=None, kwargs=None):
        Thread.__init__(self)
        self.period = period
        self.name = name
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.event = threading.Event()
        self.lock = threading.Lock()

        if self.name:
            self.setName(self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def stop(self):
        """Stop the timer if it hasn't finished yet."""
        self.event.set()
        if self.lock.locked():
            self.lock.release()
        self.stop_while = True

    def run(self):
        while self.is_alive() and not self.stop_while:
            res = self.event.wait(self.period)
            if not self.event.is_set():
                self.handler()

    '''For subclass:
    def handler(self):
        with self.lock:
            if not self.stop_while:
                return 1
    '''
    def handler(self):
        pass