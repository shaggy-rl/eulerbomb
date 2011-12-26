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