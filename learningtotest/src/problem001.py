from euler import filter
from time import time

class problem001():
    def __init__(self):
        self.start = time()
        self.answer = filter(1000,[3,5])
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 1: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem001().answer