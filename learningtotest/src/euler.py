# Used in Number 1
def multfilter(x,y):
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

# Used in Number 3
def primefactors(x):
    """Return prime factors of x"""
    answer = []
    i = 2
    while (i <= x):
        while (x % i == 0):
            answer.append(i)
            x /= i
        i += 1
    return answer

# Used in Number 4
def ispalindrome(x):
    """Used in reduce to return the sum of a list"""
    return x == int(str(x)[::-1])
def multlist(x,y):
    """Return a list of numbers that are every multiple of x <= i < y"""
    answer = []
    i = x
    while (i < y):
        j = x
        while(j < y):
            answer.append(i * j)
            j += 1
        i += 1
    return sorted(answer)
