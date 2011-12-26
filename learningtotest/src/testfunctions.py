import unittest
from euler import multfilter
from euler import primefactors
from euler import multlist
from euler import ispalindrome
from euler import lcm

class TestSequenceFunctions(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(multfilter(10,[3,5]),23) # Example from #1
    def test_primefactors(self):
        self.assertEqual(primefactors(13195),[5,7,13,29]) # Example from #3
    def test_multlist(self):
        self.assertEqual(filter(ispalindrome,multlist(10,100))[-1],9009) # Example from #4
    def test_lcm(self):
        self.assertEqual(reduce(lcm,range(1,10)),2520) # Example from #5

if __name__ == '__main__':
    unittest.main()