import unittest
import problem001

class TestSequenceFunctions(unittest.TestCase):
    def test_problem001(self):
        self.assertEqual(problem001.problem001().answer,233168)

if __name__ == '__main__':
    unittest.main()