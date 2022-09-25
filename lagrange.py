from typing import Tuple, Collection
from dataclasses import dataclass, field
from fractions import Fraction
from math import prod

@dataclass
class Factor:
    # (x-a)
    a: int

    def __repr__(self) -> str:
        if self.a == 0:
            return "x"
        if self.a < 0:
            return f"\\left(x+{self.a}\\right)"
        return f"\\left(x-{self.a}\\right)"


class Product:   
    def __init__(self):
        self.factors = []
        self.multiple = Fraction(1, 1)


    def __repr__(self) -> str:
        if self.multiple.numerator < 0:
            multiple = f" - \\frac{{{ abs(self.multiple.numerator) }}}{{{ self.multiple.denominator }}}"
        else:
            multiple = f"\\frac{{{ self.multiple.numerator }}}{{{ self.multiple.denominator }}}"
        return multiple + "".join([repr(factor) for factor in self.factors])


@dataclass
class Sum:
    products: list[Product] = field(default_factory=list)

    def __repr__(self):
        s = ""
        for i in range(len(self.products)-1):
            s += str(self.products[i])
            if self.products[i+1].multiple.numerator > 0:
                s += " + "
        s += str(self.products[-1])
        return s


def generate_equation(*list_points: Tuple[float, float]) -> Sum:
    s = Sum()
    list_points = set(list_points) # Eliminate duplicates
    for point in list_points:
        product = 1
        factors = Product()
        for other in list_points:
            if point is other:
                continue
            factors.factors.append(Factor(other[0]))
            product *= (point[0]-other[0])
        factors.multiple = Fraction(point[1], product)
        s.products.append(factors)

    return s

def main():
    equation = generate_equation(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 8)
    )
    print(equation)

if __name__ == "__main__":
    main()