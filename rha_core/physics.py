from fractions import Fraction

class PhysicsSimulator:
    def __init__(self, system):
        self.system = system

    def harmonic_oscillator(self, x0, v0, steps, dt):
        trajectory = []
        x, v = x0, v0
        for _ in range(steps):
            a = -x
            v += a * dt
            x += v * dt
            trajectory.append(x)
        return trajectory

    def free_fall(self, h0, steps, dt):
        g = Fraction(1)  # unité harmonique
        h, v = h0, Fraction(0)
        trajectory = []
        for _ in range(steps):
            v -= g * dt
            h += v * dt
            trajectory.append(max(h, 0))
            if h <= 0:
                break
        return trajectory

    def wave_propagation(self, A, steps, dx, dt):
        from math import pi, sin
        values = []
        for n in range(steps):
            t = n * float(dt)
            values.append([float(A) * sin(2 * pi * (x * float(dx) - t)) for x in range(steps)])
        return values
