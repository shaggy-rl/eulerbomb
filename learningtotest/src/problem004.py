from euler import ispalindrome,multlist
from time import time

class problem004():
    def __init__(self):
        self.start = time()
        self.answer = filter(ispalindrome,multlist(100,1000))[-1]
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 4: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem004().answer