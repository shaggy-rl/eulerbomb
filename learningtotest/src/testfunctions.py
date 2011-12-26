import unittest
from euler import filter,primefactors

class TestSequenceFunctions(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(filter(10,[3,5]),23) # Example from #1
    def test_primefactors(self):
        self.assertEqual(primefactors(13195),[5,7,13,29]) # Example from #3

if __name__ == '__main__':
    unittest.main()