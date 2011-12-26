from euler import lcm
from time import time

class problem005():
    def __init__(self):
        self.start = time()
        self.answer = reduce(lcm,range(1,20))
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 4: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem005().answer