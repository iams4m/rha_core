# rha_core

Rational Harmonic core (Rational Harmonic Arithmetic - RHA) for numeric systems in base \( b \geq 2 \).

RHA is a universal rational framework for managing mathematical constants, sequences, and geometry across all numeric bases, with optimal harmonic coherence.

## References

- Rational Harmonic Arithmetic: The First Universal Rational Framework for Constants, Sequences, and Geometry across All Bases  
  https://zenodo.org/records/15379622

- Rational Harmonic Arithmetic in Base-7 (RHA-7): Coherence Validation, Constant Alignment, and Harmonic Prediction of Planet X  
  https://zenodo.org/records/15400342

## Modules

- `constants`: Definitions of \(\phi_b\), \(\pi_b\), \(e_b\)  
- `sequence`: Construction of the harmonic sequence \(H_n\)  
- `dynamics`: Function \(h_b(n)\), trajectory analysis  
- `transfer`: Inter-base comparison  
- `physics`: Physical simulations (oscillator, free fall, wave)  
- `export`: CSV, LaTeX export  
- `visual`: Matplotlib plots  

## Usage

```python
from rha_core import constants, sequence, dynamics

hc = constants.HarmonicConstants(7)
hs = sequence.HarmonicSequence(7).generate(10)
