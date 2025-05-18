import streamlit as st
from rha_core import constants, sequence, visual

# Interface Streamlit
st.set_page_config(page_title="RHA Explorer", layout="centered")
st.title("Explorateur RHA (Rational Harmonic Arithmetic)")

# Choix de la base et du nombre de termes
base = st.number_input("Choisir une base b ≥ 2", min_value=2, max_value=100, value=7)
n_terms = st.slider("Nombre de termes de la suite Hₙ", min_value=1, max_value=50, value=20)

# Chargement des constantes
hc = constants.HarmonicConstants(base)
st.subheader(f"Constantes harmoniques en base {base}")
st.markdown(f"φ_b = (b+1)/b = {hc.phi_b} ≈ {float(hc.phi_b):.6f}")
st.markdown(f"π_b = 11/4·φ_b = {hc.pi_b} ≈ {float(hc.pi_b):.6f}")
st.markdown(f"e_b = 19/8·φ_b = {hc.e_b} ≈ {float(hc.e_b):.6f}")

# Génération de la suite
hs = sequence.HarmonicSequence(base)
seq = hs.generate(n_terms)
st.subheader("Suite harmonique Hₙ")
st.write([f"{v} ≈ {float(v):.6f}" for v in seq])

# Visualisation
viz = visual.HarmonicVisualizer()
plot_file = "harmonic_sequence_plot.png"
viz.plot_sequence(seq, plot_file)
st.image(plot_file, caption=f"Suite Hₙ en base {base}")
