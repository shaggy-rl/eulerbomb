from euler import fib,even,listsum

class problem002():
    def __init__(self):
        self.answer = reduce(listsum,filter(even,fib(4000000)))

if __name__ == '__main__':
    print problem002().answer