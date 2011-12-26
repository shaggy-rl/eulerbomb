import unittest
import problem001
import problem002
import problem003
import problem004
import problem005

class TestSequenceFunctions(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()