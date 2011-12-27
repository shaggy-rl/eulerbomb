import unittest
from time import time

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

    def test_problem012(self):
        self.assertEqual(problem012().answer,76576500)

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

class problem097():
    def __init__(self):
        self.start = time()
        self.answer = (28433 * 2 ** 7830457 + 1) % 10 ** 10
        self.stop = time()
        if (self.stop - self.start > 60):
            self.answer = "Too much time used on number 97: " + str(self.stop - self.start)

if __name__ == '__main__':
    print "001",problem001().answer
    print "002",problem002().answer
    print "003",problem003().answer
    print "004",problem004().answer
    print "005",problem005().answer
    print "006",problem006().answer
    print "007",problem007().answer
    print "008",problem008().answer
    print "009",problem009().answer
    print "010",problem010().answer
    print "012",problem012().answer
    print "097",problem097().answer
