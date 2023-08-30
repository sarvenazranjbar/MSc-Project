from .Atom import Atom

class BasicComponent:

    def __init__(self, colour: str, size: int, en: float):
        self.colour = colour
        self.size = size
        self.group = [Atom(colour) for _ in range(size)]
        self.electronegativity = en

    @staticmethod
    def rule(cells1: "BasicComponent", cells2: "BasicComponent"):
        """
        Applies a force rule between two groups of atoms (cells1 and cells2) based on their
        electronegativities. Atoms experience a force when they are within a certain distance
        from atoms of the other group. This function updates the velocities and positions
        of the atoms based on the force they experience.
        """
        window_size = Atom.window_size
        g = cells1.get_en(cells2)
        cells1 = cells1.group
        cells2 = cells2.group
        for i in range(len(cells1)):
            fx = 0
            fy = 0
            for j in range(len(cells2)):
                a = cells1[i]
                b = cells2[j]
                dx = a.x - b.x
                dy = a.y - b.y
                d = (dx*dx + dy*dy)**0.5
                if 0 < d < 80:
                    F = g/d
                    fx += F*dx
                    fy += F*dy
            if a.vx < 0:
                fx *= -1
            if a.vy < 0:
                fy *= -1
            a.vx = (a.vx + fx)
            a.vy = (a.vy + fy)
            a.x += a.vx
            a.y += a.vy
            if a.x <= 0 or a.x >= window_size:
                a.vx *= -1
            if a.y <= 0 or a.y >= window_size:
                a.vy *= -1