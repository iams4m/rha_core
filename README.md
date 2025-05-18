# rha_core

Noyau rationnel harmonique pour systèmes numériques en base \( b \geq 2 \).

## Modules

- `constants`: Définitions de \(\phi_b\), \(\pi_b\), \(e_b\)
- `sequence`: Construction de la suite \(H_n\)
- `dynamics`: Fonction \(h_b(n)\), analyse de trajectoire
- `transfer`: Comparaison inter-base
- `physics`: Simulations physiques (oscillateur, chute libre, onde)
- `export`: Export CSV, LaTeX
- `visual`: Tracés matplotlib

## Utilisation

```python
from rha_core import constants, sequence, dynamics
hc = constants.HarmonicConstants(7)
hs = sequence.HarmonicSequence(7).generate(10)
