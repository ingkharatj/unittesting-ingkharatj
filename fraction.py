import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator is not 0 :
            gcd = math.gcd(self.numerator,self.denominator)
            self.numerator = self.numerator/gcd
            self.denominator = self.denominator/gcd
        
               
            

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        a = int(self.numerator)
        b = int(self.denominator)
        c = int(frac.numerator)
        d = int(frac.denominator)

        new_num = (a*d) + (b*c)
        new_denom = b*d
        
        return Fraction(new_num,new_denom)
    
    def __sub__(self,frac):

        a = int(self.numerator)
        b = int(self.denominator)
        c = int(frac.numerator)
        d = int(frac.denominator)

        new_num = (a*d) - (b*c)
        new_denom = b*d
       
        return Fraction(new_num,new_denom)
    
    def __mul__(self,frac):
        a = int(self.numerator)
        b = int(self.denominator)
        c = int(frac.numerator)
        d = int(frac.denominator)

        new_num = a*c
        new_denom = b*d

        return Fraction(new_num,new_denom)
    
          
    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator/self.denominator}"


    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
    
        if self.numerator == frac.numerator and self.denominator == frac.denominator:
            return True
        else:
            return False
        

    