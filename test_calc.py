import unittest
import calc

# to run test, open cmd and type:
# python -m unittest test_(pythonfilename but not in bracket)
# so in this case python -m unittest test_calc.py
# however if __name__ == '__main__':
#   unittest.main() 
# use this code to run test
# python test_calc.py
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, -5), 5)
        self.assertEqual(calc.add(10, -8), 2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 9), 1)
        self.assertEqual(calc.subtract(10, 15), -5)
        self.assertEqual(calc.subtract(10, 10), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, 10), 1)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()