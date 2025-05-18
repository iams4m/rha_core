from fractions import Fraction

class HarmonicConstants:
    def __init__(self, base: int):
        if base < 2:
            raise ValueError("Base must be ≥ 2.")
        self.b = base
        self.phi_b = Fraction(base + 1, base)
        self.pi_b = Fraction(11, 4) * self.phi_b
        self.e_b = Fraction(19, 8) * self.phi_b

    def __repr__(self):
        return (f"HarmonicConstants(base={self.b}, "
                f"phi_b={self.phi_b}, pi_b={self.pi_b}, e_b={self.e_b})")
