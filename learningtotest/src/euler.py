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
def fib(x,start = 0, stop = 1):
    """Return a list of fibbonaci numbers under x"""
    answer = [start,stop]
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

# Used in Number 4
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

# Used in Number 5
def gcd(x,y):
    """Return greatest common denominator, iterative solution"""
    while (y != 0):
        (x,y) = (y,x%y)
    return x

# Used in Number 5
def lcm(x,y):
    """Return least common multiple"""
    return x * y / gcd(x,y)

# Used in Number 6
def sumofsquares(start,stop):
    """Return the sum of the squares"""
    i = start
    answer = 0
    while (i <= stop):
        answer += i ** 2
        i += 1
    return answer

# Used in Number 6
def squareofsums(start,stop):
    """Return the square of the summation"""
    i = start
    answer = 0
    while (i <= stop):
        answer += i
        i += 1
    return answer ** 2

# Used in Number 7
def thismanyprimes(x):
    """Return the first x primes"""
    answer = [2]
    i = 3
    while (len(answer) < x):
        j = 0
        isprime = 1
        while (isprime == 1 and j < len(answer)):
            if (i % answer[j] == 0):
                isprime = 0
            j += 1
        if (isprime == 1):
            answer.append(i)
        i += 1
    return answer

# Used in Number 10
def primesunder(x):
    """Return primes under x"""
    answer = [2]
    i = 3
    while (answer[-1] < x):
        j = 0
        isprime = 1
        while (isprime == 1 and j < len(answer) and answer[j] ** 2 <= i):
            if (i % answer[j] == 0):
                isprime = 0
            j += 1
        if (isprime == 1):
            answer.append(i)
        i += 2
    answer.pop()
    return answer

# Used to test Number 10
def sumofprimesunder(x):
    return reduce(listsum,primesunder(x))
