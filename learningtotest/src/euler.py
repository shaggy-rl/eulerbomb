import unittest
from time import time

class Memoize: # stolen from http://code.activestate.com/recipes/52201/
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not self.memo.has_key(args):
            self.memo[args] = self.fn(*args)
        return self.memo[args]

class TestSequenceFunctions(unittest.TestCase):
    def test__filter(self):
        self.assertEqual(multfilter(10,[3,5]),23) # Example from #1

    def test__fib(self):
        answer = []
        i = 0
        while (len(answer) < 10):
            i += 1
            answer = fib(i,1,2)
        self.assertEqual(fib(i,1,2),[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) # Example from #2

    def test__primefactors(self):
        self.assertEqual(primefactors(13195),[5,7,13,29]) # Example from #3
        self.assertEqual(primefactors(29),[29]) # Example from #3

    def test__even(self):
        self.assertEqual(even(13195),False)
        self.assertEqual(even(-10),True)
        self.assertEqual(even(-9),False)

    def test__multlist(self):
        self.assertEqual(filter(ispalindrome,multlist(10,100))[-1],9009) # Example from #4

    def test__lcm(self):
        self.assertEqual(reduce(lcm,range(1,10)),2520) # Example from #5

    def test__numberchain(self):
        self.assertEqual(numberchain(44),False)
        self.assertEqual(numberchain(32),False)
        self.assertEqual(numberchain(13),False)
        self.assertEqual(numberchain(10),False)
        self.assertEqual(numberchain(1),False)
        self.assertEqual(numberchain(85),True)
        self.assertEqual(numberchain(89),True)
        self.assertEqual(numberchain(145),True)
        self.assertEqual(numberchain(42),True)
        self.assertEqual(numberchain(20),True)
        self.assertEqual(numberchain(4),True)
        self.assertEqual(numberchain(16),True)
        self.assertEqual(numberchain(37),True)
        self.assertEqual(numberchain(58),True)

    def test__divisors(self):
        # Example from 12
        self.i = trianglenumbers()
        self.assertEqual(divisors(self.i.next()),[1])
        self.assertEqual(divisors(self.i.next()),[1,3])
        self.assertEqual(divisors(self.i.next()),[1,2,3,6])
        self.assertEqual(divisors(self.i.next()),[1,2,5,10])
        self.assertEqual(divisors(self.i.next()),[1,3,5,15])
        self.assertEqual(divisors(self.i.next()),[1,3,7,21])
        self.assertEqual(divisors(self.i.next()),[1,2,4,7,14,28])

    def test__squareofsums(self):
        self.assertEqual(squareofsums(1,10),3025) # Example from #6

    def test__sumofsquares(self):
        self.assertEqual(sumofsquares(1,10),385) # Example from #6

    def test__testmethodforsix(self):
        self.assertEqual(abs(sumofsquares(1,10)-squareofsums(1,10)),2640) # Example from #6

    def test__thismanyprimes(self):
        self.assertEqual(thismanyprimes(6),[2,3,5,7,11,13]) # Example from #7

    def test__sumofprimesunder(self):
        self.assertEqual(sumofprimesunder(10),17) # Example from #10

    def test__triangle(self):
        self.answer = []
        self.i = 1
        self.nexttri = trianglenumbers()
        while (len(self.answer) < 10):
            self.answer.append(self.nexttri.next())
        self.assertEqual(self.answer,[1,3,6,10,15,21,28,36,45,55])

    # Once I have the correct answer, make sure I don't break it later
    def test_problem001(self):
        self.assertEqual(problem001().answer,233168)

    def test_problem002(self):
        self.assertEqual(problem002().answer,4613732)
    
    def test_problem003(self):
        self.assertEqual(problem003().answer,6857)
    
    def test_problem004(self):
        self.assertEqual(problem004().answer,906609)
    
    def test_problem005(self):
        self.assertEqual(problem005().answer,232792560)
    
    def test_problem006(self):
        self.assertEqual(problem006().answer,25164150)
    
    def test_problem007(self):
        self.assertEqual(problem007().answer,104743)
    
    def test_problem008(self):
        self.assertEqual(problem008().answer,40824)
    
    def test_problem009(self):
        self.assertEqual(problem009().answer,31875000)
    
    def test_problem010(self):
        self.assertEqual(problem010().answer,142913828922)

    def test_problem011(self):
        self.assertEqual(problem011().answer,70600674)

    def test_problem012(self):
        self.assertEqual(problem012().answer,76576500)

    def test_problem092(self):
        self.assertEqual(problem092().answer,8581146)

    def test_problem097(self):
        self.assertEqual(problem097().answer,8739992577)

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

def numberchain(x):
    """The next element in the chain is the sum of the squares of the digits of the current element"""
    if (x == 1):
        return False
    if (x == 89):
        return True
    total = 0
    while (x > 0):
        total += (x % 10) ** 2
        x /= 10
    return numberchain(total)

numberchain = Memoize(numberchain)

def numberchainstart(x):
    """The next element in the chain is the sum of the squares of the digits of the current element"""
    if (x == 1):
        return False
    if (x == 89):
        return True
    total = 0
    while (x > 0):
        total += (x % 10) ** 2
        x /= 10
    return numberchain(total)

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

def primes():
    """Prime number generator"""
    yield 2
    primes = [2]
    i = 3
    while (1):
        j = 0
        isprime = 1
        while (isprime == 1 and j < len(primes) and primes[j] ** 2 <= i):
            if (i % primes[j] == 0):
                isprime = 0
            j += 1
        if (isprime == 1):
            primes.append(i)
            yield i
        i += 1

# Used in Number 7
def thismanyprimes(x):
    """Return the first x primes"""
    nextprime=primes()
    answer = [nextprime.next()]
    while (len(answer) < x):
        answer.append(nextprime.next())
    return answer

# Used in Number 10
def primesunder(x):
    """Return primes under x"""
    nextprime=primes()
    answer = [nextprime.next()]
    while (answer[-1] < x):
        answer.append(nextprime.next())
    answer.pop()
    return answer

# Used to test Number 10
def sumofprimesunder(x):
    """Return the sum of the primes under x"""
    return reduce(listsum,primesunder(x))

class problem001():
    def __init__(self):
        self.start = time()
        self.answer = multfilter(1000,[3,5])
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 1: " + str(self.stop - self.start)

class problem002():
    def __init__(self):
        self.start = time()
        self.answer = reduce(listsum,filter(even,fib(4000000)))
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 2: " + str(self.stop - self.start)

class problem003():
    def __init__(self):
        self.start = time()
        self.answer = primefactors(600851475143)[-1]
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 3: " + str(self.stop - self.start)

class problem004():
    def __init__(self):
        self.start = time()
        self.answer = filter(ispalindrome,multlist(100,1000))[-1]
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 4: " + str(self.stop - self.start)

class problem005():
    def __init__(self):
        self.start = time()
        self.answer = reduce(lcm,range(1,20))
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 5: " + str(self.stop - self.start)

class problem006():
    def __init__(self):
        self.start = time()
        self.answer = abs(sumofsquares(1,100)-squareofsums(1,100))
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 6: " + str(self.stop - self.start)

class problem007():
    def __init__(self):
        self.start = time()
        self.answer = thismanyprimes(10001)[-1]
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 7: " + str(self.stop - self.start)

class problem008():
    def __init__(self):
        self.start = time()
        self.variable = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
        self.i = 0
        self.answer = 0
        while (self.i + 4 < len(self.variable)):
            self.temp = int(self.variable[self.i]) * int(self.variable[self.i + 1]) * int(self.variable[self.i + 2]) * int(self.variable[self.i + 3]) * int(self.variable[self.i + 4])
            if (self.temp > self.answer):
                self.answer = self.temp
            self.i += 1
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 8: " + str(self.stop - self.start)

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
                self.b += 1
            self.a += 1
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 9: " + str(self.stop - self.start)

class problem010():
    def __init__(self):
        self.start = time()
        self.answer = sumofprimesunder(2000000)
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 10: " + str(self.stop - self.start)

class problem011():
    def __init__(self):
        self.start = time()
        string = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

        max = 0

        list = string.split()
        i = 0
        while(i<len(list)):
            list[i]=int(list[i])
            i += 1
    
        # Horizontal

        i = 0
        while (i+4<len(list)):
            if (i%20!=19 and i%20!=18 and i%20!=17):
                if (list[i]*list[i+1]*list[i+2]*list[i+3]>max):
                    max = list[i]*list[i+1]*list[i+2]*list[i+3]
            i += 1

        # Vertical

        i = 0
        while (i+60<len(list)):
            if (list[i]*list[i+20]*list[i+40]*list[i+60]>max):
                max = list[i]*list[i+20]*list[i+40]*list[i+60]
            i += 1

        # \

        i = 0
        while (i+63<len(list)):
            if (i%20!=19 and i%20!=18 and i%20!=17):
                if (list[i]*list[i+21]*list[i+42]*list[i+63]>max):
                    max = list[i]*list[i+21]*list[i+42]*list[i+63]
            i += 1

        # /

        i = 0
        while (i+63<len(list)):
            if (i%20!=0 and i%20!=1 and i%20!=2):
                if (list[i]*list[i+19]*list[i+38]*list[i+57]>max):
                    max = list[i]*list[i+19]*list[i+38]*list[i+57]
            i += 1

        self.answer = max
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 11: " + str(self.stop - self.start)

# Used in problem 12
def divisors(x):
    """Return the divisors of x"""
    if (x == 1):
        return [1]
    i = 1
    answer = []
    while (i * i <= x):
        if (x % i == 0):
            answer.append(i)
            answer.append(x / i)
        i += 1
    if (answer[-1] == answer[-2]):
        answer.pop()
    return sorted(answer)

# Used in problem 12
def trianglenumbers():
    """A generator that yields trianglular numbers"""
    i = 1
    while (1):
        yield i * (i + 1) / 2
        i += 1

class problem012():
    def __init__(self):
        self.start = time()
        self.divisors = []
        self.tri = trianglenumbers()
        while (len(self.divisors)<=500):
            self.answer = self.tri.next()
            self.divisors=divisors(self.answer)
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 12: " + str(self.stop - self.start)

class problem092():
    def __init__(self):
        self.start = time()
#        self.answer = len(filter(numberchainstart,range(1,10000000)))
        i = 1
        self.answer = 0
        while (i < 10000000):
            if (numberchainstart(i)):
                self.answer += 1
            i += 1
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 92: " + str(self.stop - self.start)

class problem097():
    def __init__(self):
        self.start = time()
        self.answer = (28433 * 2 ** 7830457 + 1) % 10 ** 10
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 97: " + str(self.stop - self.start)

if __name__ == '__main__':
    import euler
    i = 0
    while (i < 400):
        j = str(i)
        while (len(j) < 3):
            j = "0" + j
        try:
            j = getattr(euler,"problem"+j)
            if (j):
                run = j()
                print i,(run.stop - run.start),run.answer
        except:
            pass
        i += 1
