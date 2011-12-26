from euler import sumofprimesunder
from time import time

class problem010():
    def __init__(self):
        self.start = time()
        self.answer = sumofprimesunder(2000000)
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 10: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem010().answer