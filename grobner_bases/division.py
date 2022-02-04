from polynomial import Polynomial, Monomial

def division_schema_check(nvar, dividend, divisors):
    """
    Helper function to check that the input parameters to the
    Division constructor are valid.
    """
    try:
        assert isinstance(nvar, int)
        assert isinstance(dividend, Polynomial)
        assert isinstance(divisors, list)
        assert nvar > 0
        assert nvar == dividend.nvar
        assert len(divisors) > 0
        for divisor in divisors:
            assert isinstance(divisor, Polynomial)
            assert nvar == divisor.nvar
            assert not divisor.is_zero()

        return True

    except AssertionError:
        print(
            "Invalid division specification. Initializing zero divided by x."
        )

        return False

    
class Division(object):
    """
    A class to represent the process of Generalized 
    Polynomial Division, as outlined in Dummit and 
    Foote p.320.
    _____________________________________________________________
    Parameters:
    nvar - a positive integer for the number of indeterminates
    dividend - a Polynomial object to be divided
    divisors - a list of nonzero Polynomial objects to divide by
    _____________________________________________________________
    Methods:
    
    """
    
    def __init__(self, nvar, dividend, divisors):
        """Check schema and initialize division."""
        if division_schema_check(nvar, dividend, divisors):
            self.nvar = nvar
            self.dividend = dividend
            self.divisors = divisors
        else:
            self.nvar = 1
            self.dividend = Polynomial(1, [0], [(0,)])
            self.divisors = [Polynomial(1, [1], [(1,)])]

    def __repr__(self):
        """String representation of the division."""
        repr_str = (
            self.dividend.__repr__() +
            " / {" +
            ", ".join([divisor.__repr__() for divisor in self.divisors]) +
            "}"
        )

        return repr_str
