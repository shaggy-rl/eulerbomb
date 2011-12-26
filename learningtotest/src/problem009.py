from time import time

class problem009():
    def __init__(self):
        self.start = time()
        self.a = 1
        done = 0
        while (done == 0 and self.a <= 1000):
            self.b = self.a + 1
            while (done == 0 and self.a + self.b <= 1000):
                self.c = 1000 - self.a - self.b
                if (done == 0 and self.b < self.c):
                    if (self.a ** 2 + self.b ** 2 == self.c ** 2 and self.a + self.b + self.c == 1000):
                        done = 1
                        self.answer = self.a * self.b * self.c
                    self.c += 1
                self.b += 1
            self.a += 1
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 9: " + str(self.stop - self.start)

if __name__ == '__main__':
    print problem009().answer