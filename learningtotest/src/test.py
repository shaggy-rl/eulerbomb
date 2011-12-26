import unittest
import problem001
import problem002
import problem003
import problem004
import problem005
import problem006
import problem007
import problem008
import problem009
import problem010

from euler import multfilter
from euler import fib
from euler import primefactors
from euler import multlist
from euler import ispalindrome
from euler import lcm
from euler import sumofsquares
from euler import squareofsums
from euler import thismanyprimes
from euler import sumofprimesunder

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

    def test_sumofprimesunder(self):
        self.assertEqual(sumofprimesunder(10),17) # Example from #10

    # Once I have the correct answer, make sure I don't break it later
    def test_problem001(self):
        self.assertEqual(problem001.problem001().answer,233168)

    def test_problem002(self):
        self.assertEqual(problem002.problem002().answer,4613732)
    
    def test_problem003(self):
        self.assertEqual(problem003.problem003().answer,6857)
    
    def test_problem004(self):
        self.assertEqual(problem004.problem004().answer,906609)
    
    def test_problem005(self):
        self.assertEqual(problem005.problem005().answer,232792560)
    
    def test_problem006(self):
        self.assertEqual(problem006.problem006().answer,25164150)
    
    def test_problem007(self):
        self.assertEqual(problem007.problem007().answer,104743)
    
    def test_problem008(self):
        self.assertEqual(problem008.problem008().answer,40824)
    
    def test_problem009(self):
        self.assertEqual(problem009.problem009().answer,31875000)
    
    def test_problem010(self):
        self.assertEqual(problem010.problem010().answer,142913828922)

if __name__ == '__main__':
    unittest.main()