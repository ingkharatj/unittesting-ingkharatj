import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0)
        self.assertEqual("0",f.__str__())
        f = Fraction(0,0)
        self.assertEqual("0/0",f.__str__())
    
    def test__init__(self):
        f = Fraction(0)
        self.assertEqual(0,f.numerator)
        self.assertEqual(1,f.denominator)

        f = Fraction(1,0)
        self.assertEqual(1,f.numerator)
        self.assertEqual(0,f.denominator)

        f = Fraction(1,2)
        self.assertEqual(1,f.numerator)
        self.assertEqual(2,f.denominator)

        f = Fraction(4,8)
        self.assertEqual(1,f.numerator)
        self.assertEqual(2,f.denominator)

        f = Fraction(23,13)
        self.assertEqual(23,f.numerator)
        self.assertEqual(13,f.denominator)

        f = Fraction(-7)
        self.assertEqual(-7,f.numerator)
        self.assertEqual(1,f.denominator)
        
        f = Fraction(3,-8)
        self.assertEqual(3,f.numerator)
        self.assertEqual(-8,f.denominator)

        f = Fraction(-5,6)
        self.assertEqual(-5,f.numerator)
        self.assertEqual(6,f.denominator)

        f = Fraction(-5,10)
        self.assertEqual(-1,f.numerator)
        self.assertEqual(2,f.denominator)


        
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(5,9), Fraction(4,9)+Fraction(1,9))
        self.assertEqual(Fraction(3,2),Fraction(1)+Fraction(1,2))
        self.assertEqual(Fraction(-4,7),Fraction(1,7)+Fraction(-5,7))


    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        
        a = Fraction(0,2)
        b = Fraction(0,3)
        c = Fraction(-1,0)
        d = Fraction(-1,0)
        self.assertTrue(a==b)

        self.assertTrue(c==d)

        self.assertFalse(a==c)

