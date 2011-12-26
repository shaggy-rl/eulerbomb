import unittest
from euler import multfilter,primefactors,multlist,ispalindrome

class TestSequenceFunctions(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(multfilter(10,[3,5]),23) # Example from #1
    def test_primefactors(self):
        self.assertEqual(primefactors(13195),[5,7,13,29]) # Example from #3
    def test_multlist(self):
        self.assertEqual(filter(ispalindrome,multlist(10,100))[-1],9009)

if __name__ == '__main__':
    unittest.main()