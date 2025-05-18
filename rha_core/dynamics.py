from fractions import Fraction

class HarmonicDynamics:
    def __init__(self, base: int):
        self.base = base

    def h_b(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        result = sum(d ** 2 for d in digits)
        return result

    def analyze_trajectory(self, n: int, max_steps: int = 1000):
        seen = set()
        trajectory = []
        for _ in range(max_steps):
            if n in seen:
                break
            seen.add(n)
            trajectory.append(n)
            n = self.h_b(n)
        return {
            "length": len(trajectory),
            "cycle_start": n if n in trajectory else None,
            "cycle_length": 0 if n not in trajectory else trajectory.index(n),
            "cycle": trajectory[trajectory.index(n):] if n in trajectory else []
        }
