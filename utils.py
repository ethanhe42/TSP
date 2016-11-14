import time

class timer:
    def __init__(self):
        self.t = 0

    def tic(self):
        self.t = time.time()

    def toc(self):
        print 'secs', time.time()-self.t
        self.t = time.time()
