def polynomial_schema_check(nvar, coefficients, multidegrees):
    """
    Helper function to check that the input parameters to the 
    Polynomial constructor are valid.
    """
    try:
        assert isinstance(nvar, int)
        assert isinstance(coefficients, list)
        assert isinstance(multidegrees, list)
        
        assert nvar > 0
        assert len(coefficients) == len(multidegrees)
        
        for md in multidegrees:
            assert isinstance(md, tuple)
            assert len(md) == nvar
            assert isinstance(md[0], int)
            for d in md:
                assert d >= 0

        return True
    
    except AssertionError:
        print(
            "Invalid polynomial specification. Initializing zero polynomial."
        )

        return False


class Polynomial(object):
    """
    A class to represent multivariate polynomials over 
    the rational field.
    _________________________________________________________________
    Parameters: 
    nvar - a positive integer for the number of indeterminates
    coefficients - a list of rational coefficients corresponding 
                   to the multidegree of the given term
    multidegrees - a list of nvar-tuples of integers representing
                   the multidegree of each monomial term
    NOTE: these are converted to tuples (resp. tuples of nvar-tuples)
          upon successful initialization
    _________________________________________________________________
    Methods:
    full_multidegree - multidegree of the polynomial (i.e. 
                       multidegree of the leading term of 
                       the polynomial)
    degree - degree of the polynomial (i.e. sum of the multidegree
             of the polynomial)
    leading_coefficient - leading coefficient of the polynomial (i.e.
                          the coefficient of the term with highest 
                          multidegree)
    leading_term - leading term of the polynomial (i.e. the term
                   with the highest multidegree)
    """
    
    def __init__(self, nvar, coefficients, multidegrees):
        """Check schema and initialize polynomial.""" 
        if polynomial_schema_check(nvar, coefficients, multidegrees):
            self.nvar = nvar
            self.coefficients, self.multidegrees = zip(
                *sorted(
                    zip(coefficients, multidegrees),
                    key = lambda x: tuple(-d for d in x[1])
                )
            )
        else:
            self.nvar = 1
            self.coefficients = (0,)
            self.multidegrees = ((0,),)
            
    def __repr__(self):
        """String representation of the polynomial."""
        if self.is_zero():
            return "0"
        
        repr_str = ""
        if self.coefficients[0] < 0:
            repr_str += "-"
        for i in range(len(self.coefficients)):
            if self.coefficients[i] == 0:
                continue
            if abs(self.coefficients[i]) != 1:
                repr_str += f"{abs(self.coefficients[i])}"
            for j in range(self.nvar):
                if self.multidegrees[i][j] == 0:
                    continue
                repr_str += f"x_{j+1}"
                if self.multidegrees[i][j] > 1:
                    repr_str += f"^{self.multidegrees[i][j]}"
            if i + 1 < len(self.coefficients):
                if self.coefficients[i + 1] < 0:
                    repr_str += "-"
                elif self.coefficients[i + 1] > 0:
                    repr_str += "+"
        return repr_str

    def __eq__(self, other):
        """Check equality against another polynomial."""
        return (
            self.nvar == other.nvar and
            self.coefficients == other.coefficients and
            self.multidegrees == self.multidegrees
        )
    
    def full_multidegree(self):
        """Multidegree of the polynomial."""
        return self.multidegrees[0]

    def degree(self):
        """Degree of the polynomial."""
        return sum(self.full_multidegree())

    def leading_coefficient(self):
        """Leading coefficient of the polynomial."""
        return self.coefficients[0]

    def leading_term(self):
        """Leading term of the polynomial."""
        return Monomial(
            self.nvar,
            self.leading_coefficient(),
            self.full_multidegree()
        )

    def is_zero(self):
        return self.coefficients == (0,)

class Monomial(Polynomial):
    """
    A class to represent multivariate monomials over 
    the rational field.
    _________________________________________________________________
    Parameters: 
    nvar - a positive integer for the number of indeterminates
    coefficient - a single rational coefficient of the given monomial
    multidegree - a single nvar-tuple of integers representing the
                  multidegree of the monomial
    _________________________________________________________________
    Methods:
    None
    """
    
    def __init__(self, nvar, coefficient, multidegree):
        super().__init__(nvar, [coefficient], [multidegree])
        self.coefficient = coefficient
        self.multidegree = multidegree
