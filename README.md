# rha_core

Noyau rationnel harmonique (Rational Harmonic Arithmetic - RHA) pour systèmes numériques en base \( b \geq 2 \).

RHA est un cadre universel rationnel pour la gestion des constantes mathématiques, des suites et de la géométrie sur toutes bases numériques, avec une cohérence harmonique optimale.

## Références

- Rational Harmonic Arithmetic: The First Universal Rational Framework for Constants, Sequences, and Geometry across All Bases  
  https://zenodo.org/records/15379622  

- Rational Harmonic Arithmetic in Base-7 (RHA-7): Coherence Validation, Constant Alignment, and Harmonic Prediction of Planet X  
  https://zenodo.org/records/15400342  

## Modules

- `constants` : Définitions de \(\phi_b\), \(\pi_b\), \(e_b\)  
- `sequence` : Construction de la suite \(H_n\)  
- `dynamics` : Fonction \(h_b(n)\), analyse de trajectoire  
- `transfer` : Comparaison inter-base  
- `physics` : Simulations physiques (oscillateur, chute libre, onde)  
- `export` : Export CSV, LaTeX  
- `visual` : Tracés matplotlib  

## Utilisation

```python
from rha_core import constants, sequence, dynamics

hc = constants.HarmonicConstants(7)
hs = sequence.HarmonicSequence(7).generate(10)
