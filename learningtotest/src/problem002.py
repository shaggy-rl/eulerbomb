from euler import fib,even,listsum
from time import time

class problem002():
    def __init__(self):
        self.start = time()
        self.answer = reduce(listsum,filter(even,fib(4000000)))
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 2: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem002().answer
