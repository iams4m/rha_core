from fractions import Fraction
from typing import List

class HarmonicSystem:
    def __init__(self, base: int):
        if base <= 1:
            raise ValueError("Base must be greater than 1.")
        self.base = base
        self._phi_b = Fraction(base + 1, base)
        self._pi_b = Fraction(11, 4) * self._phi_b
        self._e_b = Fraction(19, 8) * self._phi_b

    @property
    def phi_b(self): return self._phi_b
    @property
    def pi_b(self): return self._pi_b
    @property
    def e_b(self): return self._e_b

    def harmonic_sequence(self, n: int) -> List[Fraction]:
        if n < 0: raise ValueError("n must be non-negative")
        seq = [Fraction(self.base)]
        if n >= 1:
            seq.append(Fraction(self.base + 1))
        for i in range(2, n + 1):
            seq.append(seq[i - 1] + seq[i - 2])
        return seq
