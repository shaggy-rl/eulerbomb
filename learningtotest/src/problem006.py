from euler import sumofsquares,squareofsums
from time import time

class problem006():
    def __init__(self):
        self.start = time()
        self.answer = abs(sumofsquares(1,100)-squareofsums(1,100))
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 6: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem006().answer