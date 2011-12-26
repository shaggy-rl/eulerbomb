import unittest
from euler import multfilter
from euler import fib
from euler import primefactors
from euler import multlist
from euler import ispalindrome
from euler import lcm
from euler import sumofsquares
from euler import squareofsums
from euler import thismanyprimes

class TestSequenceFunctions(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(multfilter(10,[3,5]),23) # Example from #1

    def test_fib(self):
        answer = []
        i = 0
        while (len(answer) < 10):
            i += 1
            answer = fib(i,1,2)
        self.assertEqual(fib(i,1,2),[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) # Example from #2

    def test_primefactors(self):
        self.assertEqual(primefactors(13195),[5,7,13,29]) # Example from #3

    def test_multlist(self):
        self.assertEqual(filter(ispalindrome,multlist(10,100))[-1],9009) # Example from #4

    def test_lcm(self):
        self.assertEqual(reduce(lcm,range(1,10)),2520) # Example from #5

    def test_squareofsums(self):
        self.assertEqual(squareofsums(1,10),3025) # Example from #6

    def test_sumofsquares(self):
        self.assertEqual(sumofsquares(1,10),385) # Example from #6

    def test_testmethodforsix(self):
        self.assertEqual(abs(sumofsquares(1,10)-squareofsums(1,10)),2640) # Example from #6

    def test_thismanyprimes(self):
        self.assertEqual(thismanyprimes(6),[2,3,5,7,11,13]) # Example from #7

if __name__ == '__main__':
    unittest.main()