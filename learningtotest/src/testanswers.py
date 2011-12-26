import unittest
import problem001
import problem002

class TestSequenceFunctions(unittest.TestCase):
    def test_problem001(self):
        self.assertEqual(problem001.problem001().answer,233168)
    def test_problem002(self):
        self.assertEqual(problem002.problem002().answer,4613732)

if __name__ == '__main__':
    unittest.main()