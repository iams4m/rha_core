from fractions import Fraction

class HarmonicSequence:
    def __init__(self, base: int):
        self.base = base
        self.seq = []

    def generate(self, n: int):
        if n < 0:
            raise ValueError("n must be ≥ 0.")
        H = [Fraction(self.base), Fraction(self.base + 1)]
        for _ in range(2, n + 1):
            H.append(H[-1] + H[-2])
        self.seq = H
        return H

    def get_fractions(self):
        return [f"{x.numerator}/{x.denominator}" for x in self.seq]
