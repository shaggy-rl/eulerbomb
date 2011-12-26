from euler import thismanyprimes
from time import time

class problem007():
    def __init__(self):
        self.start = time()
        self.answer = thismanyprimes(10001)[-1]
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 7: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem007().answer