import unittest
from five import Calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        c = Calc(2,5)
        self.assertEqual(c.add(), 7)
        c = Calc(-1,1)
        self.assertEqual(c.add(), 0)
        c = Calc(-1,-1)
        self.assertEqual(c.add(), -2)

    def test_sub(self):
        c = Calc(5,2)
        self.assertEqual(c.sub(), 3)
        c = Calc(-1,1)
        self.assertEqual(c.sub(), -2)
        c = Calc(-1,-1)
        self.assertEqual(c.sub(), 0)

    def test_mul(self):
        c = Calc(2,5)
        self.assertEqual(c.mul(), 10)
        c = Calc(-1,1)
        self.assertEqual(c.mul(), -1)
        c = Calc(-1,-1)
        self.assertEqual(c.mul(), 1)

    def test_div(self):
        c = Calc(2,5)
        self.assertEqual(c.div(), 0.4)
        c = Calc(-1,1)
        self.assertEqual(c.div(), -1)
        c = Calc(-1,-1)
        self.assertEqual(c.div(), 1)


if __name__ == '__main__':
    unittest.main()