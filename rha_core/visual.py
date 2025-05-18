import matplotlib.pyplot as plt

class HarmonicVisualizer:
    def plot_sequence(self, seq, filename):
        y = [float(v) for v in seq]
        plt.figure()
        plt.plot(y, marker='o')
        plt.title("Suite H_n")
        plt.savefig(filename)
        plt.close()

    def plot_trajectory(self, traj, filename):
        plt.figure()
        plt.plot(traj, marker='.')
        plt.title("Trajectoire h_b(n)")
        plt.savefig(filename)
        plt.close()

    def plot_wave(self, data, filename):
        import numpy as np
        plt.imshow(np.array(data), cmap='viridis', aspect='auto')
        plt.title("Propagation d'onde")
        plt.savefig(filename)
        plt.close()
