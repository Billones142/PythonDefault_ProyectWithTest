import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        val= calc.add(3, 7)
        self.assertEqual(val, 10)


if(__name__ == '__main__'):
    unittest.main()