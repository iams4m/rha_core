import unittest
from rha_core import core
from fractions import Fraction


class TestHarmonicSystem(unittest.TestCase):
    def test_phi_b(self):
        hs = core.HarmonicSystem(7)
        self.assertEqual(hs.phi_b, Fraction(8, 7))

    def test_pi_b(self):
        hs = core.HarmonicSystem(7)
        self.assertEqual(hs.pi_b, Fraction(22, 7))

    def test_e_b(self):
        hs = core.HarmonicSystem(7)
        self.assertEqual(hs.e_b, Fraction(19, 7))

if __name__ == '__main__':
    unittest.main()
