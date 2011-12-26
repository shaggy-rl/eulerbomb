import unittest
from euler import filter

class TestSequenceFunctions(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(filter(10,[3,5]),23) # Example from #1

if __name__ == '__main__':
    unittest.main()