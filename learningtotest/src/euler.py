# Used in Number 1
def filter(x,y):
    """Return total of integers under x that are multiples of any value in y"""
    i = 1
    answer = 0
    while (i < x):
        test = 0
        for j in y:
            if (i % j == 0):
                test = 1
        if (test == 1):
            answer += i
        i += 1
    return answer

# Used in Number 2
def fib(x):
    """Return a list of fibbonaci numbers under x"""
    answer = [0,1]
    while (answer[-1] < x):
        answer.append(answer[-1] + answer[-2])
    answer.pop()
    return answer

# Used in Number 2
def even(x):
    """Return true if x is even"""
    return x % 2 == 0

# Used in Number 2
def listsum(x,y):
    """Used in reduce to return the sum of a list"""
    return x + y
