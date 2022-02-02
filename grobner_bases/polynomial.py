class Polynomial(object):

    def __init__(self, nvar, coefficients, multidegrees):
        assert nvar > 0
        assert len(coefficients) == len(multidegrees)
        for md in multidegrees:
            assert len(md) == nvar

        self.nvar = nvar
        self.coefficients, self.multidegrees = zip(
            *sorted(
                zip(coefficients, multidegrees),
                key = lambda x: tuple(-d for d in x[1])
            )
        )

    def __repr__(self):
        repr_str = ""
        if self.coefficients[0] < 0:
            repr_str += "-"
        for i in range(len(self.coefficients)):
            repr_str += f"{abs(self.coefficients[i])}"
            for j in range(self.nvar):
                repr_str += f"x_{j+1}^{self.multidegrees[i][j]}"
            if i + 1 < len(self.coefficients):
                if self.coefficients[i + 1] < 0:
                    repr_str += "-"
                else:
                    repr_str += "+"
        return repr_str

    def full_multidegree(self):
        return self.multidegrees[0]

    def degree(self):
        return sum(self.full_multidegree())

    def leading_coefficient(self):
        return self.coefficients[0]

    def leading_term(self):
        return Monomial(
            self.nvar,
            self.leading_coefficient(),
            self.full_multidegree()
        )

class Monomial(Polynomial):

    def __init__(self, nvar, coefficient, multidegree):
        super().__init__(nvar, [coefficient], [multidegree])
        self.coefficient = coefficient
        self.multidegree = multidegree
        
