from fractions import Fraction

class BaseTransfer:
    def __init__(self, phi_b):
        self.phi_b = phi_b

    def transfer(self, quantity: Fraction, new_base: int):
        new_phi = Fraction(new_base + 1, new_base)
        return quantity * (new_phi / self.phi_b)

    def compare_bases(self, expr_name: str, base_range: range):
        expr = {
            "phi_b": lambda b: Fraction(b + 1, b),
            "pi_b": lambda b: Fraction(11, 4) * Fraction(b + 1, b),
            "e_b": lambda b: Fraction(19, 8) * Fraction(b + 1, b),
        }.get(expr_name)

        if expr is None:
            raise ValueError("Unknown expression")

        return {b: expr(b) for b in base_range}
