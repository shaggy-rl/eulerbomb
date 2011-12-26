from euler import primefactors
from time import time

class problem003():
    def __init__(self):
        self.start = time()
        self.answer = primefactors(600851475143)[-1]
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 3: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem003().answer